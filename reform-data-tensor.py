import numpy as np 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--address', type=str)
args = parser.parse_args()

def reform(wf):
    wf_zeros = np.zeros(350)
    zero_count = 0
    zeros_chn_numbers = [4,5,6,12,13,20,28,35,36,42,43,44,
                         53,54,55,61,62,69,77,84,85,91,92,93]
    reformed = []
    for i in range(98):
        if i in zeros_chn_numbers:
            reformed.append(wf_zeros)
            zero_count += 1
        else:
            reformed.append(wf[i-zero_count])
    return np.array(reformed)

path = args.address.split('/')
event = np.load('/nfs/slac/g/'+'/'.join(path[7:]))['arr_0']
event = event.reshape(74,350)

new_wf = reform(event)
new_wf = new_wf.reshape(98, 350,1)

save_path = '/nfs/slac/g/exo_data8/exo_data/users/shaolei/train_data/phase2_new_tensor/'
save_address = '/gpfs/slac/staas/fs1/g/exo/exo_data8/exo_data/users/shaolei/train_data/phase2_new_tensor/'
save_path = save_path + '/'.join(path[13:15])
save_address = save_address +'/'.join(path[13:])
isExist = os.path.exists(save_path)
if not isExist:
    os.makedirs(save_path)
np.savez(save_path + '/' + path[-1],new_wf)
print('Done.')
