source /nfs/slac/g/exo_data4/users/maweber/software/Devel/setup.sh;
cd /nfs/slac/g/exo/shaolei/GAN_trainset/;
python CreateTrainTestSet.py --inputFile '/nfs/slac/g/exo-userdata/users/shaolei/data_reweight/Co/APDWFSignalsEnergyThreshold_47*_Flattened.csv' --outFile '/nfs/slac/g/exo-userdata/users/shaolei/data_reweight/Co_WF.csv'