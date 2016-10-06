import numpy as np
import vbhmm.util as util
from vbhmm.hmm import VB_HMM
from nose.tools import assert_equal, ok_, nottest


@nottest
def test_logsum():
    pass


@nottest
def test_normalize():
    pass


@nottest
def test_KL_Dirichlet():
    pass


def test_lnZ_Dirichlet():
    upi = np.ones(10) * 0.5
    wpi = np.array(upi)
    actual = util.lnZ_Dirichlet(wpi)
    ok_(2.54 < actual < 2.55)


@nottest
def test_lnZ_Wishart():
    nu = 0.1
    model = VB_HMM(3)
    mu = np.array([[3.0, 3.0], [0.0, 0.0], [-4.0, 0.0]])
    cv = np.tile(np.identity(2), (3, 1, 1))
    z, o2 = model.simulate(50 * 10, mu, cv)
    V = np.atleast_2d(np.cov(o2.T)) * 10
    lnZ = util.lnZ_Wishart(nu, V)
    #ok_(3.9 < lnZ < 4.0)
    pass


@nottest
def test_log_like_Gauss():
    pass


@nottest
def test__sym_quad_form():
    pass


@nottest
def test_E_lndetW_Wishart():
    pass


@nottest
def test_KL_Wishart():
    pass


@nottest
def test_KL_GaussWishart():
    pass


@nottest
def test_sample_gaussian():
    pass
