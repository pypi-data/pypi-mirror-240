"""
Implements the adaptation mechanism of PSO described in [1].

References
----------
[1] Z. H. Zhan, J. Zhang, Y. Li and H. S. H. Chung, "Adaptive Particle Swarm
    Optimization," in IEEE Transactions on Systems, Man, and Cybernetics, Part B
    (Cybernetics), vol. 39, no. 6, pp. 1362-1381, Dec. 2009,
    doi: 10.1109/TSMCB.2009.2015956.
"""

import numba as nb
import numpy as np

from vpso.math import batch_cdist_and_pdist
from vpso.typing import Array1d, Array2d, Array3d


@nb.njit(
    nb.float64[:, :](nb.float64[:]),
    cache=True,
    nogil=True,
)
def adaptation_strategy(f: Array1d) -> Array2d:
    """Picks the adaptation strategy for each problem based on the ratio of average
    distances between particles and to the best particle.

    Parameters
    ----------
    f : 1d array
        Array of shape `N`.

    Returns
    -------
    2d array
        Array of shape `(N, 2)`. Each row contains the adaptation strategy for the
        `i`-th problem. The first column contains the adaptation strategy for `c1` and
        the second column contains the adaptation strategy for `c2`.
    """
    f = f[:, np.newaxis]  # add a dimension for broadcasting

    # NOTE: fails in numba's npython mode
    # deltas = np.full((f.size, 2), (-1.0, 1.0), dtype=f.dtype)  # initialize all to S4
    deltas = np.full((f.size, 2), -1.0)  # initialize all to S4 (fill in two steps)
    deltas[:, 1].fill(1.0)

    deltas = np.where(f <= 23 / 30, [(1.0, -1.0)], deltas)  # S1
    deltas = np.where(f < 0.5, [(0.5, -0.5)], deltas)  # S2
    deltas = np.where(f < 7 / 30, [(0.5, 0.5)], deltas)  # S3
    return deltas


@nb.njit(
    nb.types.UniTuple(nb.float64[:, :, :], 3)(
        nb.float64[:, :, :],  # px
        nb.float64[:, :, :],  # sx
        nb.int32,  # nvec
        nb.int32,  # swarmize
        nb.float64[:, :, :],  # lb
        nb.float64[:, :, :],  # ub
        nb.float64[:, :, :],  # w
        nb.float64[:, :, :],  # c1
        nb.float64[:, :, :],  # c2
        nb.types.NumPyRandomGeneratorType("NumPyRandomGeneratorType"),
    ),
    cache=True,
    nogil=True,
)
def adapt(
    px: Array3d,
    sx: Array3d,
    nvec: int,
    swarmsize: int,
    lb: Array3d,
    ub: Array3d,
    w: Array3d,
    c1: Array3d,
    c2: Array3d,
    np_random: np.random.Generator,
) -> tuple[Array3d, Array3d, Array3d]:
    """Performs the adaptation of the parameters `w`, `c1` and `c2` based on the
    stage of the algorithm.

    Parameters
    ----------
    px : 3d array
        Best positions of the particles so far. An array of shape `(N, M, d)`, where `N`
        is the number of vectorized problems to solve simultaneously, `M` the number of
        particle, and `d` is the dimension of the search space.
    sx : 3d array
        Social best, i.e., the best particle so far. An array of shape `(N, 1, d)`.
    nvec : int
        Number of vectorized problems.
    swarmsize : int
        Number of particles in the swarm.
    lb : 3d array
        Lower bound of the search space. An array of shape `(N, 1, d)`.
    ub : 3d array
        Upper bound of the search space. An array of shape `(N, 1, d)`.
    w : 3d array
        Inertia weight. An array of shape `(N, 1, 1)`, where each element is used for
        the corresponding problem.
    c1 : 3d array
        Cognitive weight. An array of shape `(N, 1, 1)`, where each element is used for
        the corresponding problem.
    c2 : 3d array
        Social weight. An array of shape `(N, 1, 1)`, where each element is used for
        the corresponding problem.
    np_random : np.random.Generator
        Random number generator.

    Returns
    -------
    tuple of 3d arrays
        The newly adapted parameters `w`, `c1` and `c2`.
    """
    domain = ub - lb
    G_, D_ = batch_cdist_and_pdist(px / domain, sx / domain, "euclidean")
    G = G_[:, :, 0].sum(1) / swarmsize
    D = D_.sum(2) / (swarmsize - 1)
    # NOTE: cannot run Dmin = D.min(1) and Dmax = D.max(1) in numba, so we use
    # https://stackoverflow.com/a/71214489/19648688
    Dmin = np.take_along_axis(D, D.argmin(1)[:, np.newaxis], 1)[:, 0]
    Dmax = np.take_along_axis(D, D.argmax(1)[:, np.newaxis], 1)[:, 0]
    stage = (G - Dmin) / (Dmax - Dmin + 1e-32)

    # adapt w
    w = (1 / (1 + 1.5 * np.exp(-2.6 * stage)))[:, np.newaxis, np.newaxis]

    # adapt c1 and c2
    deltas = adaptation_strategy(stage) * np_random.uniform(
        0.05, 0.1, size=(nvec, np.int32(1))
    )
    c1 = (c1 + deltas[:, 0, np.newaxis, np.newaxis]).clip(1.5, 2.5)
    c2 = (c2 + deltas[:, 1, np.newaxis, np.newaxis]).clip(1.5, 2.5)
    sum_c = c1 + c2
    mask = sum_c > 4
    c1 = np.where(mask, 4 * c1 / sum_c, c1)
    c2 = np.where(mask, 4 * c2 / sum_c, c2)
    return w, c1, c2
