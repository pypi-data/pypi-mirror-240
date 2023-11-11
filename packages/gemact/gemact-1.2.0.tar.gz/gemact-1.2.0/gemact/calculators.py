from .libraries import *
from . import helperfunctions as hf
from . import config
from .distributions import PWC

quick_setup()
logger = log.name('calculators')


class LossModelCalculator:
    """
    Calculation methods used in LossModel and Severity classes. 
    Python informal static class.
    """

    def __init__():
        pass

    @staticmethod
    def fast_fourier_transform(severity, frequency, n_aggr_dist_nodes, discr_step, tilt, tilt_value, normalize=False):
        """
        Aggregate loss distribution via Fast Fourier Transform.

        :param severity: discretized severity, nodes sequence and discrete probabilities.
        :type severity: ``dict``
        :param frequency: frequency model (adjusted).
        :type frequency: ``Frequency``
        :param n_aggr_dist_nodes: number of nodes in the approximated aggregate loss distribution.
        :type n_aggr_dist_nodes: ``int``
        :param discr_step: severity discretization step.
        :type discr_step: ``float``
        :param tilt_value: tilting parameter value of FFT method for the aggregate loss distribution approximation.
        :type tilt_value: ``float``
        :param tilt: whether tilting of FFT is present or not.
        :type tilt: ``bool``
        :return: aggregate loss distribution empirical pmf, cdf, nodes
        :rtype: ``dict``
        """
        
        fj = severity['fj']
        harr = np.arange(0, n_aggr_dist_nodes, step=1, dtype=np.int64)

        if tilt:
            tilting_par = 20 / n_aggr_dist_nodes if (tilt_value == 0) else tilt_value
        else:
            tilting_par = 0

        fj = np.append(fj, np.repeat(0, n_aggr_dist_nodes - fj.shape[0]))
        
        f_hat = fft(np.exp(-tilting_par * harr) * fj)
        g_hat = frequency.model.pgf(f=f_hat)
        g = np.exp(tilting_par * harr) * np.real(ifft(g_hat))

        if normalize:
            g = g / np.sum(g)

        cum_probs = np.minimum(np.sort(np.cumsum(g)), 1) # avoid numerical issues float numbers
        
        if (1 - cum_probs[-1]) > config.PROB_TOLERANCE:
            message = 'Failure to obtain a cumulative distribution function close to 1. '\
                'Last calculated cumulative probability is %s.' % ("{:.4f}".format(cum_probs[-1]))
            logger.warning(message)

        return {'cdf': cum_probs,
                'nodes': discr_step * harr}

    @staticmethod
    def panjer_recursion(frequency, severity, n_aggr_dist_nodes, discr_step, normalize=False):
        """
        Aggregate loss distribution via Panjer recursion.

        :param severity: discretized severity, nodes sequence and discrete probabilities.
        :type severity: ``dict``
        :param frequency: frequency model (adjusted).
        :type frequency: ``Frequency``
        :param n_aggr_dist_nodes: number of nodes in the approximated aggregate loss distribution.
        :type n_aggr_dist_nodes: ``int``
        :param discr_step: severity discretization step.
        :type discr_step: ``float``
        :return: aggregate loss distribution empirical pdf, cdf, nodes
        :rtype: ``dict``
        """
        
        fj = severity['fj']
        a, b, p0, g = frequency.abp0g0(fj)

        fj = np.append(fj, np.repeat(0, n_aggr_dist_nodes - fj.shape[0]))

        fpmf = frequency.model.pmf(1)
        for j in range(1, n_aggr_dist_nodes):
            g = np.insert(g,
            0, # position
            (np.sum(
                ((a + b * np.arange(1, j + 1) / j) * fj[1:(j+1)] * g[:j]))
                )
            )
        g = ((fpmf - (a + b) * p0) * fj + g[::-1]) / (1 - a * fj[0])
        
        if normalize:
            g = g / np.sum(g)
        
        cum_probs = np.minimum(np.sort(np.cumsum(g)), 1) # avoid numerical issues float numbers
        
        if (1 - cum_probs[-1]) > config.PROB_TOLERANCE:
            message = 'Failure to obtain a cumulative distribution function close to 1. '\
                'Last calculated cumulative probability is %s.' % ("{:.4f}".format(cum_probs[-1]))
            logger.warning(message)

        return {'cdf': cum_probs,
                'nodes': discr_step * np.arange(0, n_aggr_dist_nodes, step=1, dtype=np.int64)}

    @staticmethod
    def mc_simulation(severity, frequency, cover, deductible, n_sim, random_state):
        """
        Aggregate loss distribution via Monte Carlo simulation.

        :param severity: severity model.
        :type severity: ``Severity``
        :param frequency: frequency model (adjusted).
        :type frequency: ``Frequency``
        :param cover: cover, also referred to as limit.
        :type cover: ``int`` or ``float``
        :param deductible: deductible, also referred to as retention or priority.
        :type deductible: ``int`` or ``float``
        :param n_sim: number of simulations.
        :type n_sim: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :return: aggregate loss distribution empirical pdf, cdf, nodes.
        :rtype: ``dict``
        """
                
        p0 = severity.model.cdf(deductible) if deductible > 1e-05 else 0.

        fqsample = frequency.model.rvs(n_sim, random_state=random_state)        
        np.random.seed(random_state+1)
        svsample = severity.model.ppf(
            np.random.uniform(low=p0, high=1.0, size=int(np.sum(fqsample)))
        )
        svsample = np.minimum(svsample - deductible, cover)
        # cumsum excluding last entry as not needed in subsequent row calculation
        cs = np.cumsum(fqsample).astype(int)[:(n_sim-1)]
        xsim = np.stack([*map(np.sum, np.split(svsample, cs))])

        x_ = np.unique(xsim)
        cdf_ = hf.ecdf(xsim)(x_)

        return {'cdf': cdf_,
                'nodes': x_}

    @staticmethod
    def qmc_simulation(severity, frequency, cover, deductible, n_sim, random_state, sequence):
        """
        Aggregate loss distribution via quasi-Monte Carlo simulation.
        See scipy.stats.qmc.

        :param severity: severity model.
        :type severity: ``Severity``
        :param frequency: frequency model (adjusted).
        :type frequency: ``Frequency``
        :param cover: cover, also referred to as limit.
        :type cover: ``int`` or ``float``
        :param deductible: deductible, also referred to as retention or priority.
        :type deductible: ``int`` or ``float``
        :param n_sim: number of simulations.
        :type n_sim: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :param sequence: type of low-discrepancy sequence. One of 'halton', Halton (van der Corput), 'sobol' Sobol, and 'lhs' Latin hypercube.
        :type sequence: ``str``
        :return: aggregate loss distribution empirical pdf, cdf, nodes.
        :rtype: ``dict``
        """

        p0 = severity.model.cdf(deductible) if deductible > 1e-05 else 0.

        # QMC sampler
        if sequence == 'halton':
            sampler = qmc.Halton(d=1, seed=random_state)
        elif sequence == 'sobol':
            sampler = qmc.Sobol(d=1, seed=random_state)
        else: # sequence == 'lhs':
            sampler = qmc.LatinHypercube(d=1, seed=random_state)

        fqsample = frequency.model.ppf(sampler.random(n=n_sim).ravel())
        u = sampler.random(n=int(np.sum(fqsample))).ravel() * (1 - p0) + p0
        np.random.shuffle(u)
        svsample = np.minimum(severity.model.ppf(u) - deductible, cover)

        # cumsum excluding last entry as not needed in subsequent row calculation
        cs = np.cumsum(fqsample).astype(int)[:(n_sim-1)]
        xsim = np.stack([*map(np.sum, np.split(svsample, cs))])

        x_ = np.unique(xsim)
        cdf_ = hf.ecdf(xsim)(x_)

        return {'cdf': cdf_,
                'nodes': x_}

    @staticmethod
    def mass_dispersal(severity, deductible, discr_step, n_discr_nodes):
        """
        Severity discretization according to the mass dispersal method.

        :param severity: severity model.
        :type severity: ``Severity``
        :param deductible: deductible, also referred to as retention or priority.
        :type deductible: ``int`` or ``float``
        :param discr_step: severity discretization step.
        :type discr_step: ``float``
        :param n_discr_nodes: number of nodes of the discretized severity.
        :type n_discr_nodes: ``int``
        :return: discrete severity, nodes sequence and discrete probabilities.
        :rtype: ``dict``
        """
        corr = 1 / severity.model.sf(deductible)
        jarr = np.arange(0, n_discr_nodes) # j arr, from 0, 1, 2, ..., n_discr_nodes-1
        hj = (jarr * discr_step)[1:-1]
        fj = np.concatenate((
            np.array(severity.model.cdf(deductible + discr_step / 2) - severity.model.cdf(deductible)), 
            np.array(severity.model.cdf(deductible + hj + discr_step / 2) - severity.model.cdf(deductible + hj - discr_step / 2)),
            np.array(1 - severity.model.cdf(deductible + (n_discr_nodes-1)*discr_step - discr_step / 2))),
            axis=None, dtype="float64").ravel()
        # Correction Fx(x-0) see footnote mass dispersal of Klugman, Panjer, Willmot, Loss Models.
        fj *= corr # truncate at deductible
        nodes = severity.loc + jarr * discr_step
        return {'nodes': nodes, 'fj': fj}

    @staticmethod
    def lower_discretization(severity, deductible, discr_step, n_discr_nodes):
        """
        Severity discretization according to the lower discretization method.

        :param severity: severity model.
        :type severity: ``Severity``
        :param deductible: deductible, also referred to as retention or priority.
        :type deductible: ``int`` or ``float``
        :param discr_step: severity discretization step.
        :type discr_step: ``float``
        :param n_discr_nodes: number of nodes of the discretized severity.
        :type n_discr_nodes: ``int``
        :return: discrete severity, nodes sequence and discrete probabilities.
        :rtype: ``dict``
        """
        corr = 1 / severity.model.sf(deductible)
        
        jarr = np.arange(0, n_discr_nodes) # j arr, from 0, 1, 2, ..., n_discr_nodes-1
        hj = (jarr * discr_step)

        fj = np.concatenate((
            # first is 0, given the fact that we truncate below the deductible
            np.array([0]),
            np.array(severity.model.cdf(deductible + hj[1:]) - severity.model.cdf(deductible + hj[:-1]))
            ),
            axis=None, dtype="float64").ravel()

        # Add tail mass to last point s.t. it sums to 1
        fj[-1] = fj[-1] + severity.model.sf(deductible + hj[-1])
        fj *= corr
        nodes = severity.loc + jarr * discr_step
        return {'nodes': nodes, 'fj': fj}

    @staticmethod
    def upper_discretization(severity, deductible, discr_step, n_discr_nodes):
        """
        Severity discretization according to the upper discretization method.

        :param severity: severity model.
        :type severity: ``Severity``
        :param deductible: deductible, also referred to as retention or priority.
        :type deductible: ``int`` or ``float``
        :param discr_step: severity discretization step.
        :type discr_step: ``float``
        :param n_discr_nodes: number of nodes of the discretized severity.
        :type n_discr_nodes: ``int``
        :return: discrete severity, nodes sequence and discrete probabilities.
        :rtype: ``dict``
        """
        # de facto it truncates at deductible
        corr = 1 / severity.model.sf(deductible)
        jarr = np.arange(0, n_discr_nodes) # j arr, from 0, 1, 2, ..., n_discr_nodes-1
        hj = (jarr * discr_step)
        fj = np.concatenate((
            np.array(severity.model.cdf(deductible + hj[1:]) - severity.model.cdf(deductible + hj[:-1])),
            np.array(1 - severity.model.cdf(deductible + hj[-1]))),
            axis=None, dtype="float64").ravel()

        fj *= corr
        nodes = severity.loc + jarr * discr_step

        return {'nodes': nodes, 'fj': fj}

    @staticmethod
    def local_moments(severity, deductible, discr_step, n_discr_nodes):
        """
        Severity discretization according to the local moments method.

        :param severity: severity model.
        :type severity: ``Severity``
        :param deductible: deductible, also referred to as retention or priority.
        :type deductible: ``int`` or ``float``
        :param discr_step: severity discretization step.
        :type discr_step: ``float``
        :param n_discr_nodes: number of nodes of the discretized severity.
        :type n_discr_nodes: ``int``
        :return: discrete severity, nodes sequence and discrete probabilities.
        :rtype: ``dict``
        """
        jarr = np.arange(0, n_discr_nodes) # j arr, from 0, 1, 2, ..., n_discr_nodes-1
        hj = (jarr * discr_step)[1:-1]

        a = deductible - severity.loc
        b = (n_discr_nodes * discr_step) + deductible - severity.loc

        den = discr_step * severity.model.sf(deductible)
        fa = severity.model.lev(a) - severity.model.lev(a + discr_step)
        fj = 2 * severity.model.lev(
            a + hj
            ) - severity.model.lev(
            a + hj - discr_step
            ) - severity.model.lev(
            a + hj + discr_step
            )
        fb = severity.model.lev(b) - severity.model.lev(b - discr_step)

        fj = np.concatenate((
            np.array(fa / den + 1), 
            np.array(fj / den),
            np.array(fb / den)),
            axis=None, dtype="float64").ravel()
        fj[-1] = fj[-1] + (1 - np.sum(fj))

        nodes = severity.loc + np.arange(0, n_discr_nodes) * discr_step
        nodes = severity.loc + jarr * discr_step
        return {'nodes': nodes, 'fj': fj}


class MCCalculator:
    """
    Class representing the Monte Carlo (MC) algorithm calculators.
    Calculation methods used in LossAggregation. 
    Python informal static class.
    """

    def __init__():
        pass
    
    @staticmethod
    def rvs(size, random_state, copula, margins):
        """
        Random variates generator function of the sum of positive random variables.

        :param size: random variates sample size.
        :type size: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :param copula: Copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: Marginal distributions.
        :type margins: ``Margins``
        :return: sample of the sum of positive random variables.
        :rtype: ``numpy.float64`` or ``numpy.ndarray``
        """
        u_ = copula.rvs(size, random_state).T
        return np.sum(margins.ppf(u_), axis=0)

    @staticmethod
    def simulation_execute(size, random_state, copula, margins):
        """
        Execute Monte Carlo simulation to approximate the distribution of the sum of random variable with a
        given dependence structure.
        
        :param size: simulation random variates sample size.
        :type size: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :param copula: Copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: Marginal distributions.
        :type margins: ``Margins``
        :return: simulated nodes and their (empirical) cumulative probabilites.
        :rtype: ``tuple``
        """

        xsim = MCCalculator.rvs(size, random_state, copula, margins)
        nodes = np.unique(xsim) # nodes: sorted and unique values
        cumprobs = hf.ecdf(xsim)(nodes)

        return (nodes, cumprobs)


class AEPCalculator:
    """
    Class representing the AEP algorithm calculators.
    Calculation methods used in LossAggregation. 
    Python informal static class.
    """

    def __init__():
        pass

    @staticmethod
    def _mat(d):
        """
        AEP algorithm helper function.
        Generate matrix of the vectors in the {0,1}**d space.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param d: dimensionality of the space.
        :type d: ``int``
        :return: matrix of the vectors in the {0,1}**d space.
        :rtype: ``numpy.ndarray``
        """
        return hf.cartesian_product(*([np.array([0, 1])] * d)).T

    @staticmethod
    def _m(_card, d):
        """
        AEP algorithm helper function.
        Generate # Array of +1, -1, 0, indicating whether the new simpleces
        origined must be summed, subtracted or ignored, respectively.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param _card: cardinalities of matrices
        :type _card: ``numpy.ndarray``
        :param d: dimensionality of the space.
        :type d: ``int``
        :return: matrix of the vectors in the {0,1}**d space.
        :rtype: ``numpy.ndarray``
        """
        _a = (2. / (d + 1))
        output = _card.copy()
        greater = np.where(output > (1 / _a))
        equal = np.where(output == (1 / _a))
        lower = np.where(output < (1 / _a))
        output[greater] = (-1) ** (d + 1 - output[greater])
        output[equal] = 0
        output[lower] = (-1) ** (1 + output[lower])
        return output

    @staticmethod
    def _volume_calc(_b, _h, _mat, _svol, copula, margins):
        """
        AEP algorithm helper function.
        Volume calculator.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param _b: _b quantity AEP algorithm.
        :type _b: ``numpy.ndarray``
        :param _h: _h quantity AEP algorithm.
        :type _h: ``numpy.ndarray``
        :param _svol: _svol quantity AEP algorithm.
        :type _svol: ``numpy.ndarray``
        :param _mat: _mat quantity AEP algorithm.
        :type _mat: ``numpy.ndarray``
        :param copula: copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: marginal distributions.
        :type margins: ``Margins``
        :return: volumes.
        :rtype: ``numpy.ndarray``
        """
        h_ = (2. / (copula.dim + 1)) * _h
        b_ = np.expand_dims(_b.T, axis=0)
        # s_ = np.array((-1) ** (copula.dim - np.sum(AEPCalculator._mat(copula.dim), axis=1))).reshape(-1, 1)
        v_ = np.hstack((b_ + h_ * _mat))
        c_ = copula.cdf(margins.cdf(v_)).reshape(-1, _b.shape[0])
        result = np.sum(c_ * (_svol * np.sign(h_) ** copula.dim), axis=0)
        return result

    @staticmethod
    def _sn_update(_sn, _msn):
        """
        AEP algorithm helper function.
        Update ``_sn`` quantity.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.
        
        :param _sn: previous ``_sn`` value.
        :type _sn: ``numpy.ndarray``
        :param _msn: _msn quantity AEP algorithm.
        :type _msn: ``numpy.ndarray``
        :param d: dimensionality of the space.
        :type d: ``int``
        :return: updated ``_sn`` value.
        :rtype: ``numpy.ndarray``
        """
        result = np.repeat(_sn, _msn.shape[0]) * np.tile(
                    _msn,
                    _sn.shape[0]
                    )
        return result

    @staticmethod
    def _h_update(_h, _card, d):
        """
        AEP algorithm helper function.
        Update ``_h`` quantity.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param _h: previous ``_h`` value.
        :type _h: ``numpy.ndarray``
        :param _card: _card quantity AEP algorithm.
        :type _card: ``numpy.ndarray``
        :param d: dimensionality of the space.
        :type d: ``int``
        :return: updated ``_h`` value.
        :rtype: ``numpy.ndarray``
        """
        result = (1 - np.tile(_card, len(_h)) * (2. / (d + 1))) * np.repeat(_h, len(_card))
        return result

    @staticmethod
    def _b_update(_b, _h, _mat, d):
        """
        AEP algorithm helper function.
        Update ``_b`` quantity.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param _b: previous ``_b`` value.
        :type _b: ``numpy.ndarray``
        :param _h: ``_h`` value.
        :type _h: ``numpy.ndarray``
        :param d: dimensionality of the space.
        :type d: ``int``
        :return: updated ``_b`` value.
        :rtype: ``numpy.ndarray``
        """
        n = _mat.shape[0]
        mat_ = _mat.transpose()
        h_ = np.repeat(_h, n).reshape(-1, 1)
        times_ = int(h_.shape[0] / n)
        result = np.repeat(_b, n, 0)
        result = result + (2. / (d + 1)) * np.tile(h_, (1, d)) * np.tile(mat_, times_).transpose()
        return result

    @staticmethod
    def core_cdf(x, n_iter, copula, margins):
        """
        AEP algorithm to approximate cdf. Non vectorized version.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param x: quantile where the cumulative distribution function is evaluated.
        :type x: ``float``
        :param n_iter: number of algorithm iterations.
        :type n_iter: ``int``
        :param copula: copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: marginal distributions.
        :type margins: ``Margins``
        :return: cumulative distribution function.
        :rtype: ``float``
        """
        # initiate quantities
        _b = np.repeat(0, copula.dim).reshape(1, copula.dim)  # Vector b of the AEP algorithm.
        _h = np.array([[x]])  # Vector h of the AEP algorithm.
        _sn = np.array([1])  # Array of +1,-1, 0 indicating whether a volume must be summed,
                             # subtracted or ignored, respectively.
        _mat = AEPCalculator._mat(copula.dim) # to be filtered later? No
        _card = np.sum(_mat, axis=1)[1:] # to be filtered later or not if created after filtered _mat
        _matvol = np.expand_dims(_mat, axis=2)
        _msn =  AEPCalculator._m(_card = _card, d=copula.dim)
        fltr = _msn != 0
        _msn = _msn[fltr, ] # filtered for efficiency
        _card = _card[fltr] # filtered for efficiency
        _svol = np.array((-1) ** (copula.dim - np.sum(_mat, axis=1))).reshape(-1, 1)
        cdf = AEPCalculator._volume_calc(_b, _h, _matvol, _svol, copula, margins)[0]
        _mat = _mat[1:, ][fltr, ] # filtered for efficiency
        _vols = 0
        # start loop. n_iter reduced by 1 as _volume_calc has already been called once.
        for _ in range(n_iter-1):
            _sn = AEPCalculator._sn_update(_sn, _msn)
            _b = AEPCalculator._b_update(_b, _h, _mat, copula.dim)
            _h = AEPCalculator._h_update(_h, _card, copula.dim)
            _vols = np.sum(_sn * AEPCalculator._volume_calc(_b, _h, _matvol, _svol, copula, margins))
            cdf += _vols
        cdf += _vols * (((copula.dim + 1) ** copula.dim) / (special.factorial(copula.dim) * 2 ** copula.dim) - 1)
        return cdf

    @staticmethod
    def cdf(x, n_iter, copula, margins):
        """
        AEP algorithm to approximate cdf.
        See Arbenz P., Embrechts P., and Puccetti G.
        "The AEP algorithm for the fast computation of the distribution of the sum of dependent random variables." Bernoulli (2011): 562-591.

        :param x: quantiles where the cumulative distribution function are evaluated.
        :type x: ``float``, ``numpy.float64`` or ``numpy.ndarray``
        :param n_iter: number of algorithm iterations.
        :type n_iter: ``int``
        :param copula: Copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: Marginal distributions.
        :type margins: ``Margins``
        :return: cumulative distribution function.
        :rtype: ``numpy.float64`` or ``numpy.ndarray``
        """
        isscalar = not isinstance(x, (np.ndarray, list)) 
        x = np.ravel(x)
        output = np.empty(len(x))
        for i in range(len(output)):
            output[i] = AEPCalculator.core_cdf(x[i], n_iter, copula, margins)
        if isscalar:
            output = output.item()
        return output

    @staticmethod
    def ppf(q, n_iter, copula, margins, tol=1e-04):
        """
        Percent point function, a.k.a. the quantile function, of the random variable sum
        using AEP algorithm.
        Inverse of cumulative distribution function. See ``scipy.optimize.brentq``.
        
        :param x: quantiles where the cumulative distribution function are evaluated.
        :type x: ``float``, ``numpy.float64`` or ``numpy.ndarray``
        :param n_iter: number of AEP algorithm iterations (optional).
        :type n_iter: ``int``
        :param copula: Copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: Marginal distributions.
        :type margins: ``Margins``
        :param tol: tolerance threshold, maximum allowed absolute difference between cumulative probability values (optional).
        :type tol: ``float``
        :return: percent point function.
        :rtype: ``numpy.float64`` or ``numpy.ndarray``
        """
        hf.assert_type_value(q, 'q', logger, (float, np.ndarray, list))
        isscalar = not isinstance(q, (np.ndarray, list)) 
        q = np.ravel(q)
        output = np.empty(len(q))
        for i in range(len(output)):
            output[i] = AEPCalculator.core_ppf(q[i], n_iter, copula, margins, tol)
        if isscalar:
            output = output.item()
        return output

    @staticmethod
    def core_ppf(q, n_iter, copula, margins, tol=1e-04):
        """
        Percent point function, a.k.a. the quantile function, of the random variable sum
        using AEP algorithm. Non vectorized version.
        Inverse of cumulative distribution function. See ``scipy.optimize.brentq``.
        
        :param q: level at which the percent point function is evaluated.
        :type q: ``float``
        :param n_iter: number of AEP algorithm iterations (optional).
        :type n_iter: ``int``
        :param copula: Copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: Marginal distributions.
        :type margins: ``Margins``
        :param tol: tolerance threshold, maximum allowed absolute difference between cumulative probability values (optional).
        :type tol: ``float``
        :return: percent point function.
        :rtype: ``float`` or ``numpy.float64``
        """

        q = np.ravel(q)
        qarr = np.repeat(q, copula.dim).reshape(copula.dim, -1)
        x0 = np.sum(margins.ppf(qarr))
        diff = (q - AEPCalculator.core_cdf(x0, n_iter, copula, margins))

        if abs(diff) <= tol:
            return x0
        
        if diff < 0:
            # x0 is larger than actual q-th level quantile
            x1 = 0.5 * x0
            while AEPCalculator.core_cdf(x1, n_iter, copula, margins) > q:
                # substitute x0 with x1 as it narrows the interval
                x0 = x1
                x1 = 0.5 * x1
            bracket = [x1, x0]
        else: # diff > 0:
            # x0 is smaller than actual q-th level quantile
            x1 = 2 * x0
            while AEPCalculator.core_cdf(x1, n_iter, copula, margins) < q:
                # substitute x0 with x1 as it narrows the interval
                x0 = x1
                x1 = 2 * x1
            bracket = [x0, x1]

        output = root_scalar(lambda x : q - AEPCalculator.core_cdf(x, n_iter, copula, margins), method='brentq', bracket=bracket, xtol=tol)
        if output.converged:
            return output.root
        else:
            logger.warning('Execution of ppf failed. Result does not converged')
            return np.nan

    @staticmethod
    def rvs(size, random_state, n_iter, copula, margins, tol=1e-04):
        """
        Random variates generator function of the sum of positive random variables.

        :param size: random variates sample size.
        :type size: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :param n_iter: number of AEP algorithm iterations (optional).
        :type n_iter: ``int``
        :param copula: copula (dependence structure between margins).
        :type copula: ``Copula``
        :param margins: marginal distributions.
        :type margins: ``Margins``
        :return: sample of the sum of positive random variables.
        :rtype: ``numpy.float64`` or ``numpy.ndarray``
        """

        np.random.seed(random_state) 
        u_ = np.random.uniform(size=size)
        return AEPCalculator.ppf(u_, n_iter, copula, margins, tol)


class LossModelTowerCalculator:
    """
    Calculation methods used in LossModel class with LayerTower. 
    Python informal static class.
    """

    def __init__():
        pass

    @staticmethod
    def coverage_modifiers_adjuster(
        layer,
        loss_previous_layer,
        adjusted_exit_point,
        status
        ):
        """
        Adjust layer coverage modifiers based on layer basis.

        :param layer: layer.
        :type layer: ``np.ndarray``
        :param loss_previous_layer: loss in the layer below.
        :type loss_previous_layer: ``np.ndarray``
        :param adjusted_exit_point: adjusted exit point.
        :type adjusted_exit_point: ``np.ndarray``
        :param status: layer capacity status, i.e. 1 if not exhausted, 0 if partially or totally exhausted.
        :type status: ``np.ndarray``
        :return: adjusted_deductible and adjusted_cover.
        :rtype: ``tuple``
        """
        if layer.basis == 'regular':
            adjusted_deductible = np.repeat(layer.deductible, len(status))
            adjusted_cover = np.repeat(layer.cover, len(status))
        elif layer.basis == 'drop-down':
            adjusted_deductible = np.copy(adjusted_exit_point) # already right length
            adjusted_cover = np.repeat(layer.cover, len(status))
        elif layer.basis == 'stretch-down':
            exit_point = np.repeat(layer.cover + layer.deductible, len(status))
            adjusted_cover = exit_point - (adjusted_exit_point + loss_previous_layer) # already right length
            adjusted_cover[status] = layer.cover
            adjusted_deductible = exit_point - adjusted_cover
        return (adjusted_cover, adjusted_deductible)

    @staticmethod
    def exit_point_adjuster(
        layer,
        adjusted_cover,
        adjusted_deductible,
        status,
        ):
        """
        Adjust layer exit point based on layer basis (before eventual mainentance limit).

        :param layer: layer.
        :type layer: ``np.ndarray``
        :param adjusted_cover: adjusted cover.
        :type adjusted_cover: ``np.ndarray``
        :param adjusted_deductible: adjusted deductible.
        :type adjusted_deductible: ``np.ndarray``
        :param status: layer capacity status, i.e. 1 if not exhausted, 0 if partially or totally exhausted.
        :type status: ``np.ndarray``
        :return: adjusted_exit_point.
        :rtype: ``np.ndarray``
        """
        if layer.basis in ('drop-down', 'regular'):
            adjusted_exit_point = np.copy(adjusted_deductible)
            adjusted_exit_point[status] = (adjusted_cover + adjusted_deductible)[status]
        else: # layer.basis == 'stretch-down':
            adjusted_exit_point = adjusted_cover + adjusted_deductible
            adjusted_exit_point = adjusted_exit_point
        return adjusted_exit_point

    @staticmethod
    def tower_simulation(severity, frequency, policystructure, aggr_loss_dist_method, n_sim, random_state, sequence):
        """
        Aggregate loss distribution of tower layers.
        Approximatio via quasi-Monte Carlo or Monte Carlo simulation.

        :param severity: severity model.
        :type severity: ``Severity``
        :param frequency: frequency model.
        :type frequency: ``Frequency``
        :param policystructure: policy structure.
        :type policystructure: ``PolicyStructure``
        :param aggr_loss_dist_method: computational method to approximate the aggregate loss distribution.
                                    One of Fast Fourier Transform ('fft'),
                                    Panjer recursion ('recursion'), Monte Carlo simulation ('mc') and quasi-Monte Carlo ('qmc').
        :type aggr_loss_dist_method: ``str``
        :param n_sim: number of simulations of Monte Carlo ('mc') and of quasi-Monte Carlo ('qmc') methods for the aggregate loss distribution approximation.
        :type n_sim: ``int``
        :param random_state: random state for the random number generator in mc and qmc.
        :type random_state: ``int``
        :param qmc_sequence: type of quasi-Monte Carlo low-discrepancy sequence.
                            One of Halton - van der Corput ('halton'), Latin hypercube ('lhs'), and Sobol ('sobol'). Optional (default is 'sobol').
        :type qmc_sequence: ``str``
        :return: list of the aggregate loss distribution (PWC) of each layer.
        :rtype: ``list``
        """
        
        output = [None] * policystructure.length
        container = np.empty((policystructure.length, n_sim))

        if aggr_loss_dist_method == 'mc':
            layer_loss_container = LossModelTowerCalculator.mc_simulation_execute(
                severity, frequency, n_sim, random_state
                )
        else: # 'qmc'
            layer_loss_container = LossModelTowerCalculator.qmc_simulation_execute(
                severity, frequency, n_sim, random_state, sequence
                )

        for i in range(n_sim-1):
            layer_loss = layer_loss_container[i]
            in_layer_loss_after_agg = np.zeros(layer_loss.shape[0], dtype=np.float64)
            in_layer_loss_before_agg = np.zeros(layer_loss.shape[0], dtype=np.float64)
            
            status = np.ones(shape=len(layer_loss), dtype=bool)
            adjusted_exit_point = np.zeros(shape=len(layer_loss), dtype=np.float64)
            for k in range(policystructure.length):
                adjusted_cover, adjusted_deductible = LossModelTowerCalculator.coverage_modifiers_adjuster(
                    layer=policystructure.layers[k],
                    loss_previous_layer=in_layer_loss_after_agg,
                    adjusted_exit_point=adjusted_exit_point,
                    status=status
                )
            
                in_layer_loss_before_agg = np.minimum(
                    np.maximum(layer_loss - adjusted_deductible, 0),
                    adjusted_cover
                )
                in_layer_loss_after_agg = np.diff(
                    np.minimum(policystructure.layers[k].aggr_cover,
                    np.cumsum(in_layer_loss_before_agg)),
                    prepend=0
                )
                # update status and adjusted_exit_point for next iteration
                status = ~(in_layer_loss_after_agg < in_layer_loss_before_agg)
                adjusted_exit_point = LossModelTowerCalculator.exit_point_adjuster(
                    layer = policystructure.layers[k],
                    adjusted_cover=adjusted_cover,
                    adjusted_deductible=adjusted_deductible,
                    status=status
                )
                # adjustments in case of maintenance deductible
                if k == 0:
                    # adjust adjuster_exit_point and in_layer_loss_after_agg
                    adjusted_cover[~status] = policystructure.layers[k].maintenance_limit
                    adjusted_exit_point = adjusted_deductible + adjusted_cover
                    in_layer_loss_after_agg[~status] = np.minimum(
                        layer_loss, adjusted_cover
                    )[~status]
                # store losses in the layer container
                container[k, i] = np.sum(in_layer_loss_after_agg)
            # finally adjust retention loss if first layer is a retention layer
            if policystructure.layers[0].retention == True:
                container[0, i] += np.sum(layer_loss) - np.sum(container[:, i])

        for j in range(policystructure.length):
            x = container[j, :] * policystructure.layers[j].share
            x_ = np.unique(container[j, :])
            output[j] = PWC(
                nodes=x_, 
                cumprobs=hf.ecdf(x)(x_)
                )
        return output

    @staticmethod
    def mc_simulation_execute(severity, frequency, n_sim, random_state):
        """
        loss simulation via Monte Carlo.

        :param severity: severity model.
        :type severity: ``Severity``
        :param frequency: frequency model (adjusted).
        :type frequency: ``Frequency``
        :param n_sim: number of simulations.
        :type n_sim: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :param sequence: type of low-discrepancy sequence. One of 'halton', Halton (van der Corput), 'sobol' Sobol, and 'lhs' Latin hypercube.
        :type sequence: ``str``
        :return: aggregate loss distribution experiment realizations.
        :rtype: ``list``
        """
        fqsample = frequency.model.rvs(n_sim, random_state=random_state)
        svsample = severity.model.rvs(int(np.sum(fqsample)), random_state=random_state)
        cs = np.cumsum(fqsample).astype(int)[:(n_sim-1)]
        return np.split(svsample, cs)

    @staticmethod
    def qmc_simulation_execute(severity, frequency, n_sim, random_state, sequence):
        """
        loss simulation via quasi-Monte Carlo.
        See scipy.stats.qmc.

        :param severity: severity model.
        :type severity: ``Severity``
        :param frequency: frequency model (adjusted).
        :type frequency: ``Frequency``
        :param n_sim: number of simulations.
        :type n_sim: ``int``
        :param random_state: random state for the random number generator.
        :type random_state: ``int``
        :param sequence: type of low-discrepancy sequence. One of 'halton', Halton (van der Corput), 'sobol' Sobol, and 'lhs' Latin hypercube.
        :type sequence: ``str``
        :return: aggregate loss distribution experiment realizations.
        :rtype: ``list``
        """

        # QMC sampler
        if sequence == 'halton':
            sampler = qmc.Halton(d=1, seed=random_state)
        elif sequence == 'sobol':
            sampler = qmc.Sobol(d=1, seed=random_state)
        else: # sequence == 'lhs':
            sampler = qmc.LatinHypercube(d=1, seed=random_state)

        fqsample = frequency.model.ppf(sampler.random(n=n_sim).ravel())
        u = sampler.random(n=int(np.sum(fqsample))).ravel()
        np.random.shuffle(u)
        svsample = severity.model.ppf(u)
        cs = np.cumsum(fqsample).astype(int)[:(n_sim-1)]
        return np.split(svsample, cs)
