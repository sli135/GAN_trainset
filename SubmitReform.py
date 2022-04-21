import os
import numpy as np
train_file,train_label = 'train_small_set_file_se_2.npy','train_small_set_label_se_2.npy'
val_file,val_label = '/sdf/home/s/shaolei/generator-reweight/train_files/phase1/val_file_se.npy','/sdf/home/s/shaolei/generator-reweight/train_files/phase1/val_label_se.npy'

body = """
source /nfs/slac/g/exo_data4/users/maweber/software/Devel/setup.sh;
cd /nfs/slac/g/exo/shaolei/GAN_trainset/;
python reform-data-tensor.py --address %s ;
"""
save_parent = '/gpfs/slac/staas/fs1/g/exo/exo_data8/exo_data/users/shaolei/train_data/phase2_new_tensor/'
address = np.load(train_file)
new_train_file = []
for i,ad in enumerate(address):
    cmd = 'bsub -R rhel60 -W 72:00 -o output/new_tensor/new_tensor_%s.out python reform-data-tensor.py --address %s'%(i,ad)
    os.system(cmd)
    path = ad.split('/')
    save_address = save_parent +'/'.join(path[13:])
    new_train_file.append(save_address)
np.save('train_small_set_file_se_2_new_tensor.npy',new_train_file)