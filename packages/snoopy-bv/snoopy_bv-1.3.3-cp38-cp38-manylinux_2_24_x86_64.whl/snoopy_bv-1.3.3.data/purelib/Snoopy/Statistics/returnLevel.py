import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from Snoopy import logger
from droppy.pyplotTools import probN
from scipy.stats import beta

class ReturnLevel():
    """Compute return period from samples.

    Notes
    -----
    Assumes :
        - independent events
        - that number of events in the duration is always the same.

    All relates to the following formulae (probability of not exceeding return value on return period is 1/e) :

        $P(X_{RP}, RP) = 1 / e$

    with:

        $P(X, T) = P_c^{T / Rtz}$

    $P_c$ being the non-exceedance probability on each events (can be up-crossing period)

    $RP = - Rtz / ln( P_c(x) )$

    This is not to be used for POT, where number of threshold exceedance is random (Poisson process)
    """

    def __init__(self, data, duration, alphap = 0. , betap = 0.):
        """Construct ReturnLevel instance

        Parameters
        ----------
        data : array like
            data samples (independent events)
        duration : float
            Total duration covered by the data. If None, duration is retrieve from data index (if Series). Each event thus corresponds to DT = duration / len(data).
        alphap : float, optional
            alpha coefficient for empirical distribution. The default is 0..
        betap : float, optional
            beta coefficient for empirical distribution. The default is 0..

        Example
        ------
        >>> rl = ReturnLevel( data , duration = 10800 )
        >>> rl.rp_2_x( 3600  )
        >>> rl.plot()

        """

        self.data = data

        self._n = len(data)

        if duration is None :
            self._duration = data.index.max() - data.index.min()
        else :
            self._duration = duration


        # Empirical exceedance probabilitys
        prob = probN(self._n, alphap = alphap , betap = betap)

        # Empirical return period
        self._rp = -duration / (self._n * np.log( 1 - prob ))

        # Empirical return values
        self._rv = np.sort(data)

        # Event duration
        self.t_block = duration / self._n

        # Space for interpolator
        self._x_to_rp = None


    @staticmethod
    def pc_to_rp( pc, blockSize):
        """Convert probability of each event to return period

        $RP = - Rtz / ln( P_c(x) )$

        Parameters
        ----------
        pc : float or np.ndarray
            Non-exceedance probability of event
        blockSize : float
            Duration of the 'event'

        Returns
        -------
        float or np.ndarray
            Return period
        """
        return -blockSize / np.log( pc )

    @staticmethod
    def rp_to_pc(rp, blockSize):
        """Convert return period to probability of event.

        $RP = - Rtz / ln( P_c(x) )$

        Parameters
        ----------
        rp : float or np.ndarray
            Return period
        blockSize : float
            Duration of the 'event'

        Returns
        -------
        float or np.ndarray
            Non-exceedance probability of event
        """
        return np.exp(-blockSize / rp)

    @property
    def empirical_rp(self):
        return self._rp

    @property
    def empirical_rv(self):
        return self._rv


    def _build_interp(self):
        # Build interpolator

        logger.debug("Build return level interpolator")
        self._rp_to_x = InterpolatedUnivariateSpline( self._rp , self._rv, ext = "raise", k = 1 )

        # Handle duplicated data
        _, u_index = np.unique(self._rv, return_index=True)
        self._x_to_rp = InterpolatedUnivariateSpline( self._rv[u_index] , self._rp[u_index], ext = "raise", k = 1)


    def plot(self, ax = None, scale_rp = lambda x:x, marker = "+" , linestyle = "", transpose = False, scale_y = 1, **kwargs):
        """Plot value against return period.

        Parameters
        ----------
        ax : AxesSubplot, optional
            Where to plot. The default is None.
        scale_rp : fun, optional
            RP scale (for instance, in input data are seconds, but plots is desired in hours). The default is identity.
        marker : str, optional
            Marker. The default is "+".
        linestyle : str, optional
            linestyle. The default is "".
        transpose : bool. The default is False
            If True, Return period is on vertical axis
        **kwargs : any
            Optional argument passed to plt.plot()

        Returns
        -------
        ax : AxesSubplot
            The graph.
        """
        if ax is None :
            fig , ax = plt.subplots()

        x = scale_rp(self._rp )
        y = self._rv * scale_y
        if transpose :
            x, y = y, x
            ax.set_yscale("log")
            ax.set(ylabel = "Return period")
        else:
            ax.set_xscale("log")
            ax.set(xlabel = "Return period")

        ax.plot( x, y,  marker = marker, linestyle = linestyle, **kwargs)

        return ax

    def x_2_rp(self , x) :
        """Return period from return value

        Parameters
        ----------
        x : float
            Return value

        Returns
        -------
        float
            Return period
        """
        if self._x_to_rp is None:
            self._build_interp()
        return self._x_to_rp(x)

    def rp_2_x(self, rp) :
        """Return value from return period

        Parameters
        ----------
        rp : float
            return period

        Returns
        -------
        float
            return value
        """
        if self._x_to_rp is None:
            self._build_interp()
        return self._rp_to_x(rp)


    def x_to_rpci( self, alpha, ci_type = "n" ):
        """Return RP confidence interval for sorted empirical return values

        Parameters
        ----------
        alpha : float
            Centered confidence interval
        ci_type : TYPE, optional
            DESCRIPTION. The default is "n".

        Returns
        -------
        (np.ndarray, np.ndarray)
            Lower and upper CI.
        """

        i = np.arange(1, self._n + 1, 1)[::-1]

        if ci_type == "n" :
            betaN = beta( i , self._n + 1 - i )
        elif ci_type == "jeffrey" :
            betaN = beta( i + 0.5 , self._n + 0.5 - i )

        return betaN.ppf( alpha/2 ) , betaN.ppf(1-alpha/2)


    def plot_ci(self, alpha_ci , ax = None, scale_rp = lambda x:x, ci_type = "n", alpha = 0.1, scale_y = 1, **kwargs) :
        """Plot confidence interval

        Parameters
        ----------
        alpha_ci : float
            Centered confidence interval.
        ax : AxesSubplot, optional
            Where to plot. The default is None.
        scale_rp : fun, optional
            RP scale (for instance, in input data are seconds, but plots is desired in hours). The default is identity
        ci_type : str, optional
            Variant for the confidence interval, among ["n" , "jeffrey"]. The default is "n".
        alpha : float, optional
            Opacity for the filling of the confidence interval. The default is 0.1.
        scale_y : float
            Scale for y-axis
        **kwargs : any
            Additional arguments passed to .fillbetweenx().

        Returns
        -------
        ax : AxesSubplot
            The graph.
        """

        if ax is None :
            fig , ax = plt.subplots()

        prob_l, prob_u = self.x_to_rpci(alpha_ci, ci_type = ci_type)
        rp_l = scale_rp(-self._duration / (self._n * np.log( 1 - prob_l )) )
        rp_u = scale_rp(-self._duration / (self._n * np.log( 1 - prob_u )) )

        ax.fill_betweenx(self._rv * scale_y, rp_l, rp_u, alpha = alpha, **kwargs)
        # ax.plot( rp_l, self._rv)
        # ax.plot( rp_u, self._rv)

        return ax


    @staticmethod
    def plot_distribution( distribution, blockSize, rp_range, ax = None, scale_y = 1.0, transpose = False, **kwargs):
        """Plot analytical distribution against return period

        Parameters
        ----------
        distribution : scipy.stats.rv_frozen
            Distribution on each event.
        blockSize : float
            duration of each event
        ax : plt.Axis, optional
            Where to plot. The default is None.
        transpose : bool. The default is False
            If True, Return period is on vertical axis

        Returns
        -------
        ax : plt.Axes
            The graph
        """

        if ax is None :
            fig, ax = plt.subplots()

        x, y = rp_range, ReturnLevel.rp_to_x_distribution( distribution, blockSize, rp_range)
        y *= scale_y
        if transpose :
            y, x  = x, y
            ax.set_yscale("log")
        else :
            ax.set_xscale("log")
        ax.plot( x, y, **kwargs)
        return ax


    @staticmethod
    def x_to_rp_distribution( distribution, blockSize, x):
        """Calculate return period of a given value x. x follows "distribution" on each even that has a duration "blockSize".

        Parameters
        ----------
        distribution : scipy.stats.rv_frozen
            Distribution on each event.
        blockSize : float
            duration of each event

        x : float
            Value

        Returns
        -------
        rp : float
            return period
        """

        return -blockSize / np.log( distribution.cdf(x) )

    @staticmethod
    def slope_distribution( distribution, blockSize, rp, d_rp = 0.1 ):
        """Return distribution slope

        Parameters
        ----------
        distribution : stats.rv_frozen
            Analitycal distribution
        blockSize : float
            Block size
        rp : float
            Return period
        d_rp : float, optional
            RP step for differentiation. The default is 0.1.

        Returns
        -------
        float
            slope
        """

        x1 = ReturnLevel.rp_to_x_distribution(distribution, blockSize, rp)
        x2 = ReturnLevel.rp_to_x_distribution(distribution, blockSize, rp + d_rp)

        return (x2-x1) / ( np.log(rp+d_rp) - np.log(rp)  )


    @staticmethod
    def rp_to_x_distribution(distribution, blockSize, rp):
        """Calculate return value x from return period rp. x follows "distribution" on each even that has a duration "blockSize".

        Parameters
        ----------
        distribution : scipy.stats.rv_frozen
            Distribution on each event.
        blockSize : float
            duration of each event
        rp : float or np.ndarray
            return period

        Returns
        -------
        x : float or np.ndarray
            return value
        """
        p_ = 1 - np.exp(-blockSize / (rp))
        return distribution.isf(p_)




def xrp_pdf( x, rp, alpha, T_block, dist ):
    """Compute probability density of the empirical return value x, with return period 'rp', knowin simulated time and distribution.

    Parameters
    ----------
    x : float or np.ndarray
        Response value
    rp : float
        return value
    alpha : float
        ratio between data duration and return period
    T_block : float
        Block size (fixed event duration)
    dist : stats.rv_continuous
        Disitribution of event

    Returns
    -------
    float or np.ndarray
        Prability density of x.
    """
    nu = 1 / T_block
    p = np.exp(-1/(nu*rp))
    return dist.pdf( x ) * beta( (nu*alpha*rp+1) * p , (nu*alpha*rp+1)*(1-p) ).pdf(dist.cdf(x))


def xrp_cdf( x, rp, alpha, T_block, dist ):
    """Compute cumulative probability of the empirical return value x, with return period 'rp', knowin simulated time and distribution.

    Parameters
    ----------
    x : float or np.ndarray
        Response value
    rp : float
        return value
    alpha : float
        ratio between data duration and return period
    T_block : float
        Block size (fixed event duration)
    dist : stats.rv_continuous
        Disitribution of event

    Returns
    -------
    float or np.ndarray
        Prability density of x.
    """
    nu = 1 / T_block
    p = np.exp(-1/(nu*rp))
    return beta( (nu*alpha*rp+1) * p , (nu*alpha*rp+1)*(1-p) ).cdf( dist.cdf(x) )





