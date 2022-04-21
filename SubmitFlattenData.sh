
source /nfs/slac/g/exo_data4/users/maweber/software/Devel/setup.sh;
cd /nfs/slac/g/exo/shaolei/GAN_trainset/;
python FlattenData.py --inputFile '/nfs/slac/g/exo-userdata/users/shaolei/data_reweight/Co/APDWFSignalsEnergyThreshold_5349.csv' --plotName './pics/Co_set_5349.png' --marginFactor 5.0 > /nfs/slac/g/exo/shaolei/GAN_trainset/output/FlattenData.out 2> /nfs/slac/g/exo/shaolei/GAN_trainset/output/FlattenData.err;

