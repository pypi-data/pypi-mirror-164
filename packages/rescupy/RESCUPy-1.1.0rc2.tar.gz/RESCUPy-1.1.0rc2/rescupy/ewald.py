# -*- coding: utf-8 -*-
"""
Created on 2020-12-01

@author: Vincent Michaud-Rioux
"""

from rescupy.geometry import (
    cell_in_range,
    distmatper,
    distmatmetric,
    cartesian,
    wigner_seiz_radius,
)
from scipy.special import erfc
import numpy as np


def ewaldPotential(avec, dielectric, xyz, charge, pts):
    pi = np.pi
    epsi = dielectric
    inveps = np.linalg.inv(epsi)
    bvec = 2 * pi * np.linalg.inv(avec).T  # Reciprocal vectors
    volume = np.abs(np.linalg.det(avec))  # Unit cell volume
    natom = 1  # Number of atoms
    Z = charge

    ren = np.abs(np.linalg.det(epsi))
    qmax = Z  # Mean charge
    eta = np.sqrt(pi) / (volume / np.sqrt(ren)) ** (1 / 3)  # Gaussian width
    tol = 2.2204e-16
    terr = pi * natom**2 * qmax**2 / volume / eta**2  # Real space error prefactor
    gerr = (
        natom**2 * qmax**2 / np.sqrt(pi) * eta
    )  # Reciprocal space error prefactor
    tcut = (
        ren ** (1 / 6) * np.sqrt(-np.log(tol) + np.log(terr)) / eta
    )  # Real space cutoff
    gcut = 2 * eta * np.sqrt(-np.log(tol) + np.log(gerr))  # Reciprocal space cutoff
    # [distvec,distsca] = genvecmat(xyz(ia,:),xyz(ja,:))
    distvec, distsca = distmatmetric(pts, xyz, inveps)

    ##################### Reciprocal space sum ################################

    center = np.matmul(0.5 * np.ones((1, 3)), bvec)
    rad = np.linalg.norm(center)
    gvec = cell_in_range(center, gcut + rad, bvec, issym=True)
    gvec = np.matmul(gvec, bvec)
    gsqr = np.matmul(gvec, epsi)
    gsqr = np.sqrt(np.sum(gvec * gsqr, axis=1))

    index = np.logical_and(gsqr <= gcut, np.logical_not(np.isclose(gsqr, 0)))
    gvec = gvec[index, :]
    gsqr = gsqr[index]
    gsqr = gsqr**2
    ng = gsqr.size
    gvec = gvec[:, np.newaxis, :]

    Ewald1 = 0.0
    for ii in range(ng):
        Etmp = distvec * gvec[ii, :, :]
        Etmp = np.cos(np.sum(Etmp, axis=2))
        Etmp = 1.0 / gsqr[ii] * Etmp * np.exp(-gsqr[ii] / 4 / eta**2)
        Ewald1 += Etmp
    Ewald1 *= 4 * pi / volume * Z

    ################################ Constant terms ###########################

    Ewald2 = -pi / volume / eta**2 * Z

    # Ewald3 = -eta/np.sqrt(pi*ren)*Z

    ############################## Real space sum #############################

    center = np.matmul(0.5 * np.ones((1, 3)), avec)
    rad = np.linalg.norm(center)
    tvec = cell_in_range(center, tcut + rad, avec, issym=True)
    tvec = np.matmul(tvec, avec)
    tsqr = np.linalg.norm(tvec, axis=1)

    index = np.logical_and(tsqr <= tcut, np.logical_not(np.isclose(tsqr, 0)))
    tvec = tvec[index, :]
    tsqr = tsqr[index]
    tsqr = tsqr**2
    nt = tsqr.size

    index = distsca > 1e-12
    Ewald4 = 0.0 * Ewald1
    Ewald4[index] = erfc(eta * distsca[index]) / distsca[index]
    for ii in range(nt):
        Etmp = xyz + tvec[ii, :]
        distvec, distsca = distmatmetric(pts, Etmp, inveps)
        index = distsca > 1e-12
        Etmp = 0.0 * Ewald1
        Etmp[index] = erfc(eta * distsca[index]) / distsca[index]
        Ewald4 += Etmp
    Ewald4 *= Z / np.sqrt(ren)

    Ewald = Ewald1 + Ewald2 + Ewald4
    Ewald = Ewald.flatten()
    return Ewald, eta


def ewaldEnergy(avec, dielectric, xyz, charge):
    pi = np.pi
    p, eta = ewaldPotential(avec, dielectric, xyz, charge, xyz)

    ren = np.abs(np.linalg.det(dielectric))

    e = 0.5 * charge * p - eta / np.sqrt(pi * ren) * charge**2
    return e

    # epsi = dielectric
    # inveps = np.linalg.inv(epsi)
    # bvec = 2*pi*np.linalg.inv(avec).T # Reciprocal vectors
    # volume = np.abs(np.linalg.det(avec)) # Unit cell volume
    # natom = 1 # Number of atoms
    # Z = charge
    # qmax = Z # Mean charge
    # eta = np.sqrt(pi)/(volume/np.sqrt(ren))**(1/3) # Gaussian width
    # tol = 2.2204e-16
    # terr = pi*natom**2*qmax**2/volume/eta**2 # Real space error prefactor
    # gerr = natom**2*qmax**2/np.sqrt(pi)*eta # Reciprocal space error prefactor
    # tcut = ren**(1/6)*np.sqrt(-np.log(tol)+np.log(terr))/eta # Real space cutoff
    # gcut = 2*eta*np.sqrt(-np.log(tol)+np.log(gerr)) # Reciprocal space cutoff
    # # [distvec,distsca] = genvecmat(xyz(ia,:),xyz(ja,:))
    # distvec, distsca = distmatmetric(xyz, xyz, inveps)
    # ##################### Reciprocal space sum ################################
    # center = np.matmul(0.5*np.ones((1,3)),bvec)
    # rad = np.linalg.norm(center)
    # gvec = cell_in_range(center, gcut+rad, bvec, issym=True)
    # gvec = np.matmul(gvec, bvec)
    # gsqr = np.matmul(gvec, epsi)
    # gsqr = np.sqrt(np.sum(gvec*gsqr, axis = 1))
    # index = np.logical_and(gsqr <= gcut, np.logical_not(np.isclose(gsqr, 0)))
    # gvec = gvec[index,:]
    # gsqr = gsqr[index]
    # gsqr = gsqr**2
    # ng = gsqr.size
    # gvec = gvec[:,np.newaxis,:]
    # Ewald1 = 0.
    # for ii in range(ng):
    #     Etmp = distvec * gvec[ii,:,:]
    #     Etmp = np.cos(np.sum(Etmp, axis=2))
    #     Etmp = 1./gsqr[ii]*Etmp*np.exp(-gsqr[ii]/4/eta**2)
    #     Ewald1 += Etmp
    # Ewald1 *= 2*pi/volume*Z**2
    # ################################ Constant terms ###########################
    # Ewald2 = -pi/2/volume/eta**2*Z**2
    # Ewald3 = -eta/np.sqrt(pi*ren)*Z**2
    # ############################## Real space sum #############################
    # center = np.matmul(0.5*np.ones((1,3)), avec)
    # rad = np.linalg.norm(center)
    # tvec = cell_in_range(center, tcut+rad, avec, issym=True)
    # tvec = np.matmul(tvec, avec)
    # tsqr = np.linalg.norm(tvec, axis=1)
    # index = np.logical_and(tsqr <= tcut, np.logical_not(np.isclose(tsqr, 0)))
    # tvec = tvec[index,:]
    # tsqr = tsqr[index]
    # tsqr = tsqr**2
    # nt = tsqr.size
    # # Ewald4 = erfc(eta*distsca)/distsca
    # Ewald4 = 0.
    # for ii in range(nt):
    #     Etmp = xyz + tvec[ii,:]
    #     distvec, distsca = distmatmetric(xyz, Etmp, inveps)
    #     Etmp = erfc(eta*distsca)/distsca
    #     Ewald4 += Etmp
    # Ewald4 *= 1/2/np.sqrt(ren)*Z**2
    # Ewald = Ewald1 + Ewald2 + Ewald3 + Ewald4
    # return Ewald
