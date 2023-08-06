# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:07:51 2015

@author: Vincent
"""

import numpy as np
import scipy.spatial.distance as sdist

PI = np.pi


def cart2sphe(x, y=None, z=None):
    if y is None or z is None:
        y = x[:, 1:2]
        z = x[:, 2:3]
        x = x[:, 0:1]
    r = np.sqrt(x * x + y * y + z * z)
    phi = np.zeros_like(r)
    theta = np.zeros_like(r)
    mask = r > np.spacing(1.0)
    theta[mask] = np.arccos(z[mask] / r[mask])
    phi[mask] = np.arctan2(y[mask], x[mask])
    return np.hstack((r, theta, phi))


def sphe2cart(r, theta=None, phi=None):
    if theta is None or phi is None:
        theta = r[:, 1:2]
        phi = r[:, 2:3]
        r = r[:, 0:1]
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.hstack((x, y, z))


def MonkhorstPackNodes(nvec):
    nodes = []
    for ii in nvec:
        x = np.linspace(0, 1, num=ii, endpoint=False)
        x += np.mod(ii + 1, 2) / 2 / ii
        nodes.append(x)
    return nodes


def distmatper(a, b, avec):
    t = np.arange(-2, 3)
    txyz = cartesian((t, t, t))
    txyz = np.matmul(txyz, avec)
    D = distmat(a, b)
    for i in range(txyz.shape[0]):
        D = np.minimum(D, distmat(a, b + txyz[i, :]))
    return D


def distmat(a, b, bc=[0, 0, 0]):
    """Computes the distance matrix between two sets of points.

    If boundary
    conditions are not trivial, the domain is assumed to be periodic and the
    function returns the distance to the closest image.

    Args:
        a (2D array):
            Stack of row-vectors.
        b (2D array):
            Stack of row-vectors.
        bc (1D array):
            Domain length, if zero the domain is assumed to be infinite.

    Returns:
        dist (2D array):
            Distance matrix.
    """
    if np.any(bc):
        dist = np.abs(b[np.newaxis, :, :] - a[:, np.newaxis, :])

        if bc[0] > 0:
            index = dist[:, :, 0] > bc[0] / 2
            dist[index, 0] *= -1
            dist[index, 0] += bc[0]

        if bc[1] > 0:
            index = dist[:, :, 1] > bc[1] / 2
            dist[index, 1] *= -1
            dist[index, 1] += bc[1]

        if bc[2] > 0:
            index = dist[:, :, 2] > bc[2] / 2
            dist[index, 2] *= -1
            dist[index, 2] += bc[2]

        dist = np.linalg.norm(dist, axis=2)
    else:
        dist = sdist.cdist(a, b)
    return dist


def vectmat(a, b):
    """Computes the difference vectors between two sets of points.

    Args:
        a (2D array)
            Stack of row-vectors.
        b (2D array)
            Stack of row-vectors.

    Returns:
        dist (3D array)
            Difference vectors (along last dimension).
    """
    dist = b[:, np.newaxis, :] - a[np.newaxis, :, :]
    return dist


def distmatmetric(a, b, m):
    """Computes the difference vectors between two sets of points.

    Args:
        a (2D array)
            Stack of row-vectors.
        b (2D array)
            Stack of row-vectors.
        m (2D array)
            Metric.

    Returns:
        dist (3D array)
                Difference vectors (along last dimension).
    """
    dvec = b[:, np.newaxis, :] - a[np.newaxis, :, :]
    dist = np.einsum("ijk,kl", dvec, m)
    dist = np.sqrt(np.sum(dist * dvec, axis=2))
    return dvec, dist


def phase(nvec, avec, k):
    """Computes the k-vector phase on a real space grid.

    Args:
        nvec (1D array):
            Grid count.
        avec (2D array):
            Lattice vectors.
        k (1D array):
            K-point.

    Returns:
        ph (1D array)
            Real space phase on a grid.
    """

    gd = grid(nvec, avec)
    ph = np.exp(-1j * gd.dot(k))
    return ph


def grid(nvec, avec):
    """Computes the grid point coordinates.

    Args:
        nvec (1D array):
            Grid count.
        avec (2D array):
            Lattice vectors.

    Returns:
        gd (2D array)
            Grid points.
    """

    gd = [[] for ii in range(3)]
    for ii in range(3):
        gd[ii] = np.arange(nvec[ii]) / nvec[ii]
    gd = cartesian(gd)
    gd = gd.dot(avec)
    return gd


def circum_poly(rad, avec):
    """Computes the polyhedron defined by avec circumscribing the sphere (point, rad).

    Row-vectors are given in avec.
    The circumscribing polyhedron is centred at the same point as the sphere and
    extends +- bvec*avec

    Args:
        rad (float):
            Sphere radius.
        avec (2D array):
            Lattice vectors.

    Returns:
        bvec (1D array):
            Translation factors.
    """
    bvec = np.cross(np.roll(avec, 1, 0), np.roll(avec, -1, 0), 1)
    bvec /= np.linalg.norm(bvec, axis=1)[np.newaxis].T
    bvec = rad / np.sum(avec * bvec, 1)
    bvec = np.abs(bvec)
    return bvec


def circum_sphere(avec):
    """Computes the sphere circumscribing the polyhedron defined by avec.

    Row-vectors are given in avec.
    The circumscribing sphere is centred at the same point as the polyhedron.

    Args:
        avec (2D array):
            Lattice vectors.

    Returns:
        rad (float):
            Sphere radius.
    """
    vec = np.array([-0.5, 0.5])
    rad = cartesian([vec, vec, vec])
    rad = np.dot(rad, avec)
    rad = np.linalg.norm(rad, axis=1)
    return rad.max()


def cell_in_range(point, rad, avec, issym=False):
    """Computes the indices of the unit cells that are overlapping with the
    circumscribed polyhedron.

    Args:
        point (1D array)
            Sphere center coordinates.
        rad (float):
            Sphere radius.
        avec (2D array):
            Lattice vectors.

    Returns:
        poly (2D array)
            Interacting unit cell bounds.
    """
    # poly = circum_poly(rad, avec)
    # poly = np.vstack((-poly,poly))
    # poly = cartesian([poly[:,0],poly[:,1],poly[:,2]])
    # poly = np.dot(poly,avec)
    # poly = poly + point
    # poly = np.linalg.solve(avec.T, poly.T).T
    # poly = np.floor(poly)
    # poly = np.vstack((np.min(poly,axis=0),np.max(poly,axis=0)))
    # return poly
    rad = np.array(rad)
    redxyz = np.linalg.solve(avec.T, point.T).T  # get reduced coordinates
    bvec = np.linalg.inv(avec).T  # get normal vectors
    nrbv = np.linalg.norm(bvec, axis=1, keepdims=True)  # get norms
    bvec = bvec / nrbv  # normalized normal vectors
    proj = np.sum(
        bvec * avec, 1, keepdims=True
    )  # project lattice vectors on normal vectors
    proj = np.abs(proj)
    proj = rad.reshape((-1, 1)) / proj.T
    lbound = np.min(redxyz - proj, axis=0)
    lbound = np.floor(lbound).astype(int)  # cell numbering determined by floor
    ubound = np.max(redxyz + proj, axis=0)
    ubound = np.floor(ubound).astype(int)  # cell numbering determined by floor
    if issym:
        bound = np.maximum(np.abs(lbound), np.abs(ubound))
        lbound = -bound
        ubound = bound
    x = np.arange(lbound[0], ubound[0] + 1)
    y = np.arange(lbound[1], ubound[1] + 1)
    z = np.arange(lbound[2], ubound[2] + 1)
    return cartesian((x, y, z))


def cartesian(arrays, out=None):
    """Generates a cartesian product of input arrays.

    Source: http://stackoverflow.com/questions/1208118/using-numpy-to-build-an-array-of-all-combinations-of-two-arrays


    Args:
        arrays (list of array-like):
            1-D arrays to form the cartesian product of.
        out (ndarray):
            Arrays to place the cartesian product in.

    Returns:
        out (ndarray):
            2-D array of shape (M, len(arrays)) containing cartesian products
            formed of input arrays.
    """
    grid = np.meshgrid(*arrays, indexing="ij")
    out = [gd.reshape((gd.size, 1), order="F") for gd in grid]
    out = np.hstack(out)

    return out


def wigner_seiz_radius(avec):
    t = np.arange(-5, 6)
    txyz = cartesian((t, t, t))
    txyz = np.matmul(txyz, avec)
    index = np.logical_not(np.all(np.isclose(txyz, 0), axis=1))
    txyz = txyz[index, :]
    D = distmat(txyz, np.array([[0, 0, 0]]))
    return 0.5 * np.min(D)
