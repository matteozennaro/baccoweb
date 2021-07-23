import numpy as np
import sys
import bacco
import json

ocdm = float(sys.argv[1]) if len(sys.argv) > 1 else 0.27

pp = bacco.cosmo_parameters.Euclid
pp['omega_cdm'] = ocdm

cosmo = bacco.Cosmology(verbose=0, **pp)
k = np.logspace(-2, 0, 50)
pk = cosmo.get_powerspec(wavemode=k)
# print(k, pk)

kl = k.tolist()
pkl = pk.tolist()
data = {'k' : kl, 'pk' : pkl}
# with open('.emu_k_pk.json', 'w') as f:
#     json.dump(data, f)
print(json.dumps(data))
