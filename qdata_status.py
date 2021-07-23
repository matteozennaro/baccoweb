import matplotlib
matplotlib.use('Agg')
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import time


text = {'usetex' : False}
matplotlib.rc('text', **text)

font = {'family' : 'sans-serif',
        'weight' : 'normal'}

matplotlib.rc('font', **font)

for sim in ['nenya', 'narya', 'vilya']:

    sim0_nfw_present = []
    sim0_sdm_present = []
    sim0_sub_present = []
    sim0_orph_present = []
    sim0_halo_present = []

    simp_nfw_present = []
    simp_sdm_present = []
    simp_sub_present = []
    simp_orph_present = []
    simp_halo_present = []

    marker = 's'
    ms = 5
    mpos = [0.1,0.11,0.12,0.13,0.14]

    nsnap = 54 if sim!='nenya' else 96

    for snap in range(nsnap):

        Sim = {'nenya' : 'Nenya', 'narya' : 'Narya', 'vilya' : 'Vilya'}[sim]

        fname = '/dipc-global/cosmosims/ThreeRings/{}/{}_N4320_L1440.0_output'.format(Sim, sim)
        phase = '/0.00/'
        hfile = 'groups_{:03d}/fof_subhalo_history_tab_orph_wweight_{:03d}'.format(snap, snap)
        nfw = '._halo_nfw_pars'
        sdm = '._sdm_qdata'
        sub = '_sub.qdata'
        orph = '_orph.qdata'
        halo = '.qdata'

        sim0_nfw_present.append(os.path.isfile(fname + phase + hfile + nfw))
        sim0_sdm_present.append(os.path.isfile(fname + phase + hfile + sdm))
        sim0_sub_present.append(os.path.isfile(fname + phase + hfile + sub))
        sim0_orph_present.append(os.path.isfile(fname + phase + hfile + orph))
        sim0_halo_present.append(os.path.isfile(fname + phase + hfile + halo))

        fname = '/dipc-global/cosmosims/ThreeRings/{}/{}_N4320_L1440.0_output'.format(Sim, sim)
        phase = '/3.14/'
        hfile = 'groups_{:03d}/fof_subhalo_history_tab_orph_wweight_{:03d}'.format(snap, snap)
        nfw = '._halo_nfw_pars'
        sdm = '._sdm_qdata'
        sub = '_sub.qdata'
        orph = '_orph.qdata'
        halo = '.qdata'

        simp_nfw_present.append(os.path.isfile(fname + phase + hfile + nfw))
        simp_sdm_present.append(os.path.isfile(fname + phase + hfile + sdm))
        simp_sub_present.append(os.path.isfile(fname + phase + hfile + sub))
        simp_orph_present.append(os.path.isfile(fname + phase + hfile + orph))
        simp_halo_present.append(os.path.isfile(fname + phase + hfile + halo))

    sim0_nfw_present = np.array(sim0_nfw_present)
    sim0_sdm_present = np.array(sim0_sdm_present)
    sim0_sub_present = np.array(sim0_sub_present)
    sim0_orph_present = np.array(sim0_orph_present)
    sim0_halo_present = np.array(sim0_halo_present)

    simp_nfw_present = np.array(simp_nfw_present)
    simp_sdm_present = np.array(simp_sdm_present)
    simp_sub_present = np.array(simp_sub_present)
    simp_orph_present = np.array(simp_orph_present)
    simp_halo_present = np.array(simp_halo_present)

    fig, ax = plt.subplots(2, 1, figsize=(10,4), sharex=True, gridspec_kw={'hspace':0})

    mnfw = sim0_nfw_present.astype(np.int) != 0
    msdm = sim0_sdm_present.astype(np.int) != 0
    msub = sim0_sub_present.astype(np.int) != 0
    morph = sim0_orph_present.astype(np.int) != 0
    mhalo = sim0_halo_present.astype(np.int) != 0

    ax[0].plot(np.arange(len(sim0_sdm_present))[msdm], sim0_sdm_present.astype(np.int)[msdm] * mpos[0], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_sub_present))[msub], sim0_sub_present.astype(np.int)[msub] * mpos[1], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_orph_present))[morph], sim0_orph_present.astype(np.int)[morph] * mpos[2], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_halo_present))[mhalo], sim0_halo_present.astype(np.int)[mhalo] * mpos[3], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_nfw_present))[mnfw], sim0_nfw_present.astype(np.int)[mnfw] * mpos[4], color='forestgreen', lw=0, marker=marker, ms=ms)

    mnfw = sim0_nfw_present.astype(np.int) == 0
    msdm = sim0_sdm_present.astype(np.int) == 0
    msub = sim0_sub_present.astype(np.int) == 0
    morph = sim0_orph_present.astype(np.int) == 0
    mhalo = sim0_halo_present.astype(np.int) == 0

    ax[0].plot(np.arange(len(sim0_sdm_present))[msdm], sim0_sdm_present.astype(np.int)[msdm] + mpos[0], color='darkred', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_sub_present))[msub], sim0_sub_present.astype(np.int)[msub] + mpos[1], color='darkred', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_orph_present))[morph], sim0_orph_present.astype(np.int)[morph] + mpos[2], color='darkred', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_halo_present))[mhalo], sim0_halo_present.astype(np.int)[mhalo] + mpos[3], color='darkred', lw=0, marker=marker, ms=ms)
    ax[0].plot(np.arange(len(sim0_nfw_present))[mnfw], sim0_nfw_present.astype(np.int)[mnfw] + mpos[4], color='darkred', lw=0, marker=marker, ms=ms)

    mnfw = simp_nfw_present.astype(np.int) != 0
    msdm = simp_sdm_present.astype(np.int) != 0
    msub = simp_sub_present.astype(np.int) != 0
    morph = simp_orph_present.astype(np.int) != 0
    mhalo = simp_halo_present.astype(np.int) != 0

    ax[1].plot(np.arange(len(simp_sdm_present))[msdm], simp_sdm_present.astype(np.int)[msdm] * mpos[0], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_sub_present))[msub], simp_sub_present.astype(np.int)[msub] * mpos[1], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_orph_present))[morph], simp_orph_present.astype(np.int)[morph] * mpos[2], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_halo_present))[mhalo], simp_halo_present.astype(np.int)[mhalo] * mpos[3], color='forestgreen', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_nfw_present))[mnfw], simp_nfw_present.astype(np.int)[mnfw] * mpos[4], color='forestgreen', lw=0, marker=marker, ms=ms)

    mnfw = simp_nfw_present.astype(np.int) == 0
    msdm = simp_sdm_present.astype(np.int) == 0
    msub = simp_sub_present.astype(np.int) == 0
    morph = simp_orph_present.astype(np.int) == 0
    mhalo = simp_halo_present.astype(np.int) == 0

    ax[1].plot(np.arange(len(simp_sdm_present))[msdm], simp_sdm_present.astype(np.int)[msdm] + mpos[0], color='darkred', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_sub_present))[msub], simp_sub_present.astype(np.int)[msub] + mpos[1], color='darkred', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_orph_present))[morph], simp_orph_present.astype(np.int)[morph] + mpos[2], color='darkred', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_halo_present))[mhalo], simp_halo_present.astype(np.int)[mhalo] + mpos[3], color='darkred', lw=0, marker=marker, ms=ms)
    ax[1].plot(np.arange(len(simp_nfw_present))[mnfw], simp_nfw_present.astype(np.int)[mnfw] + mpos[4], color='darkred', lw=0, marker=marker, ms=ms)

    ax[1].set_xlabel('snapshot')
    ax[0].tick_params(axis='y', which='both', left=False, right=False, labelbottom=True)
    ax[1].tick_params(axis='y', which='both', left=False, right=False, labelbottom=True)
    ax[0].set_yticks(mpos)
    ax[0].set_yticklabels(['sdm', 'sub', 'orph', 'halo', 'nfw'])
    ax[1].set_yticks(mpos)
    ax[1].set_yticklabels(['sdm', 'sub', 'orph', 'halo', 'nfw'])

    dd = 0.2 * (mpos[-1]-mpos[0])
    ax[0].set_ylim([mpos[0]-dd, mpos[-1]+dd])
    ax[1].set_ylim([mpos[0]-dd, mpos[-1]+dd])

    plt.tight_layout()
    plt.savefig('images/{}_qdata.png'.format(sim))
