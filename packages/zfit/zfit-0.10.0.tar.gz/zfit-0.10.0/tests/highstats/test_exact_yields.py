#  Copyright (c) 2022 zfit

import matplotlib.pyplot as plt
import numpy as np
import pytest


@pytest.mark.parametrize("exact_nsample", [True, False], ids=["exact", "binomial sum"])
def test_yield_bias(exact_nsample, ntoys=100):
    import zfit
    import zfit.z.numpy as znp

    # create space
    obs = zfit.Space("x", limits=(-10, 10))
    # parameters
    mu = zfit.Parameter("mu", 1.0, -4, 6)
    sigma = zfit.Parameter("sigma", 1.1, 0.1, 10)
    lambd = zfit.Parameter("lambda", -0.06, -1, -0.01)

    # model building, pdf creation
    gauss = zfit.pdf.Gauss(mu=mu, sigma=sigma, obs=obs)
    exponential = zfit.pdf.Exponential(lambd, obs=obs)
    n_bkg = zfit.Parameter("n_bkg", 20000)
    n_sig = zfit.Parameter("n_sig", 1000)
    params = [mu, sigma, lambd, n_bkg, n_sig]
    gauss_extended = gauss.create_extended(n_sig)
    exp_extended = exponential.create_extended(n_bkg)
    model = zfit.pdf.SumPDF([gauss_extended, exp_extended])

    # set the values to a start value for the fit
    init_vals = [0.5, 1.2, -0.05, 20350, 2512]
    true_vals = [1.0, 1.1, -0.06, 20000, 3000]
    zfit.param.set_values(params, true_vals)
    true_nsig = true_vals[-1]
    gauss_sample = gauss.create_sampler(n=true_nsig)
    true_nbkg = true_vals[-2]
    exp_sample = exponential.create_sampler(n=true_nbkg)

    def sample_func():
        exp_sample.resample()
        gauss_sample.resample()
        gauss_val = gauss_sample.value()
        assert gauss_val.shape[0] == true_nsig
        exp_val = exp_sample.value()
        assert exp_val.shape[0] == true_nbkg
        return znp.concatenate([gauss_val, exp_val])

    data = model.create_sampler()
    data.sample_holder.assign(sample_func())
    nll = zfit.loss.ExtendedUnbinnedNLL(model=model, data=data)
    nsigs = []
    nbkgs = []
    minimizer = zfit.minimize.Minuit(gradient=False, tol=1e-5)
    failures = 0
    for _ in range(ntoys):
        zfit.param.set_values(params, true_vals)
        if exact_nsample:
            data.sample_holder.assign(sample_func())
        else:
            data.resample(n=sum(true_vals[-2:]))
        for _ in range(10):
            zfit.param.set_values(params, init_vals)
            rnd_sig = np.random.uniform(-(true_nsig**0.5), true_nsig**0.5)
            rnd_bkg = np.random.uniform(-(true_nbkg**0.5), true_nbkg**0.5)
            # stretch the upper part -> make it asymetric but with as many events left as right
            rnd_sig *= (rnd_sig > 0) + 1
            rnd_sig += (
                (rnd_sig > 0) - 0.5
            ) + true_nsig**0.5 / 2  # push at least half a sigma away
            rnd_bkg *= (rnd_bkg > 0) + 1
            rnd_bkg += (
                (rnd_bkg > 0) - 0.5
            ) + true_nbkg**0.5 / 2  # push at least half a sigma away
            n_sig.set_value(true_nsig + rnd_sig)
            n_bkg.set_value(true_nbkg + rnd_bkg)
            result = minimizer.minimize(nll)
            if result.valid:
                break
        else:
            failures += 1
            continue  # it didn't converge

        nsig_res = float(result.params[n_sig]["value"])
        nsigs.append(nsig_res)
        nbkg_res = float(result.params[n_bkg]["value"])
        nbkgs.append(nbkg_res)
        assert nsig_res + nbkg_res == pytest.approx(true_nsig + true_nbkg, abs=0.5)

    nsigs_mean = np.mean(nsigs)
    std_nsigs_mean = np.std(nsigs) / ntoys**0.5
    nbkg_mean = np.mean(nbkgs)
    std_nbkg_mean = np.std(nbkgs) / ntoys**0.5

    # for debugging and testing
    # print(result)
    # print("failures:", failures)
    # print(f'nsig: {nsigs_mean :.2f} +- {std_nsigs_mean :.2f}')
    # print(f'nbkg: {nbkg_mean :.2f} +- {std_nbkg_mean :.2f}')

    plt.figure("yield_bias_toys")
    plt.title(
        f'{"Exact" if exact_nsample else "Binomial sum"} sampled. Fit with {minimizer.name}. Signal yield: {nsigs_mean :.2f} +- {std_nsigs_mean:.2f}'
    )
    counts, edges, _ = plt.hist(nsigs, bins=50, label="nsig", alpha=0.5)
    npoints = 50
    plt.plot(
        np.ones(npoints) * true_nsig, np.linspace(0, np.max(counts)), "gx", label="true"
    )
    plt.plot(
        np.ones(npoints) * nsigs_mean,
        np.linspace(0, np.max(counts) * 2 / 3),
        "bo",
        label="mean",
    )

    plt.plot(
        np.ones(npoints) * nsigs_mean - np.std(nsigs),
        np.linspace(0, np.max(counts) * 0.2),
        "ro",
        label="-std",
    )
    plt.plot(
        np.ones(npoints) * nsigs_mean + np.std(nsigs),
        np.linspace(0, np.max(counts) * 0.2),
        "ro",
        label="+std",
    )
    plt.legend()
    pytest.zfit_savefig()

    rel_err_sig = 5 / true_nsig**0.5 / ntoys**0.5
    assert nsigs_mean == pytest.approx(true_nsig, rel=rel_err_sig)
    rel_err_bkg = 5 / true_nbkg**0.5 / ntoys**0.5
    assert nbkg_mean == pytest.approx(true_nbkg, rel=rel_err_bkg)
    print(f"relative error sig: {rel_err_sig}")
    print(f"relative error bkg: {rel_err_bkg}")
