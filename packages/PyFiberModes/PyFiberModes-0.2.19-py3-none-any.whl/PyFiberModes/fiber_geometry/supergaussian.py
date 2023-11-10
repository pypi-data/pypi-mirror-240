from PyFiberModes.fiber_geometry.geometry import Geometry
from math import sqrt, exp
import numpy
from scipy.special import jn, iv
from scipy.special import jvp, ivp

from scipy.integrate import ode
from scipy.constants import mu_0, epsilon_0, physical_constants
eta0 = physical_constants['characteristic impedance of vacuum']
Y0 = sqrt(epsilon_0 / mu_0)  #: Admitance of free-space.


class SuperGaussian(Geometry):

    DEFAULT_PARAMS = [0, 1e-6, 1]

    def __init__(self, ri, ro, *fp, **kwargs):
        super().__init__(ri, ro, *fp, **kwargs)
        mu, self.c, self.m = fp
        if ri == 0:
            self.mu = mu
        else:
            self.mu = (self.ro - self.ri) / 2 + self.ri + mu

    def index(self, r, wl):
        if self.ri <= abs(r) <= self.ro:

            n = self._m.n(wl, *self._mp)
            cn = self._cm.n(wl, *self._cmp)

            if r > 0 or self.ri == 0:
                a = exp(-0.5 * ((r - self.mu) / self.c)**(2*self.m))
            else:
                a = exp(-0.5 * ((r + self.mu) / self.c)**(2*self.m))

            assert a <= 1

            return cn + a * (n - cn)

        return None

    def indexp(self, r, wl):
        """First derivative of index."""
        n = self._m.n(wl, *self._mp)
        cn = self._cm.n(wl, *self._cmp)

        if r > 0 or self.ri == 0:
            power = 2 * self.m - 1
            term_0 = (cn - n) * self.m * n
            term_1 = (r - self.mu) / self.c
            return term_0 * term_1**power / self.c
        else:
            power = 2 * self.m
            term_0 = (cn - n) * self.m * n
            term_1 = (r + self.mu) / self.c
            return term_0 * term_1**power / (self.mu + r)

    def minIndex(self, wl):
        di = abs(self.mu - self.ri)
        do = abs(self.mu - self.ro)
        return self.index(self.ri if (di > do) else self.ro, wl)

    def maxIndex(self, wl):
        if self.ri <= self.mu <= self.ro:
            return self.index(self.mu, wl)

        di = abs(self.mu - self.ri)
        do = abs(self.mu - self.ro)
        return self.index(self.ri if (di < do) else self.ro, wl)

    def u(self, r, neff, wl):
        return wl.k0 * r * sqrt(abs(self.index(r, wl)**2 - neff**2))

    def EH_fields(self, ri, ro, nu, neff, wl, EH, tm=False):
        dr = 1e-10
        if ri == 0:
            # set initial condition
            ri = dr
            n = self.index(ri, wl)
            u = self.u(ri, neff, wl)
            if neff < n:
                ez = jn(nu, u)
                ezp = jvp(nu, u) * u / ri
            else:
                ez = iv(nu, u)
                ezp = ivp(nu, u) * u / ri
            hz = 0
            hzp = 0
            eza = 0
            ezap = 0
            hza = ez
            hzap = ezp
        elif nu == 0:
            ez, hz = EH
        else:
            ez, eza = EH[0]
            hz, hza = EH[1]
            # find derivatives...

        nu2 = nu * nu
        beta = wl.k0 * neff
        beta2 = beta * beta

        def f(r, y):
            """
            Bures (3.139)

            """
            assert r != 0
            r2 = r * r
            p = (wl.k0 * self.index(r, wl))**2 - beta2

            np = self.indexp(r, wl)
            n = self.index(r, wl)

            yp = numpy.empty(4)
            yp[0] = y[2]
            yp[1] = y[3]
            yp[2] = (y[0] * (nu2 / r2 - p) +
                     y[2] * (2 * beta2 / p * np / n - 1 / r) -
                     y[1] * eta0 * (2 * nu * beta * wl.k0 * np /
                                              (r * p * n)))
            yp[3] = (y[1] * (nu2 / r2 - p) +
                     y[3] * (2 * wl.k0**2 * n * np / p - 1 / r) -
                     y[0] * Y0 * (2 * nu * beta * wl.k0 * n * np /
                                            (r * p)))
            return yp

        def jac(r, y):
            r2 = r * r
            p = (wl.k0 * self.index(r, wl))**2 - beta2

            np = self.indexp(r, wl)
            n = self.index(r, wl)

            m = numpy.empty((4, 4))
            m[0, :] = (0, 0, 1, 0)
            m[1, :] = (0, 0, 0, 1)
            m[2, :] = ((nu2 / r2 - p),
                       -(eta0 * (2 * nu * beta * wl.k0 * np /
                                           (r * p * n))),
                       (2 * wl.k0**2 * n * np / p - 1 / r),
                       0)
            m[3, :] = (-Y0 * (2 * nu * beta * wl.k0 * n * np /
                                        (r * p)),
                       0,
                       (nu2 / r2 - p),
                       (2 * wl.k0**2 * n * np / p - 1 / r))
            return m

        s = ode(f, jac).set_integrator("dopri5")

        if nu == 0:
            s.set_initial_value([ez, hz, ezp, hzp], ri)
            ez, hz, ezp, hzp = s.integrate(ro)

            EH = ez, hz
            Ezp = numpy.array([ezp])
            Hzp = numpy.array([hzp])
        else:
            s.set_initial_value([ez, hz, ezp, hzp], ri)
            ez, hz, ezp, hzp = s.integrate(ro)

            s.set_initial_value([eza, hza, ezap, hzap], ri)
            eza, hza, ezap, hzap = s.integrate(ro)

            EH[0] = ez, eza
            EH[1] = hz, hza

            Ezp = numpy.array([ezp, ezap])
            Hzp = numpy.array([hzp, hzap])

        # calc ephi and hphi
        u = self.u(ro, neff, wl)
        n = self.index(ro, wl)
        beta = wl.k0 * neff
        c = 1 / (wl.k0**2 * (n * n - neff * neff))

        EH[2] = c * (beta * EH[0] * nu / ro - eta0 * wl.k0 * Hzp)

        EH[3] = c * (-beta * EH[1] * nu / ro + Y0 * wl.k0 * n * n * Ezp)

        return EH
