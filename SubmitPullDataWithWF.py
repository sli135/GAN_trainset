import ROOT
import os
import numpy as np

ROOT.gSystem.Load('../EXOEnergy/lib/libEXOEnergy.so')
ROOT.gSystem.Load("libEXOUtilities")

infoRuns = ROOT.EXOSourceRunsPolishedInfo('../EXOEnergy/data/SourceRunsInfo_Phase1_20170411.txt')
#ProcDataSet = ROOT.EXORunInfoManager.GetDataSet("Data/Processed/masked", "run>=5100&&run<=5200")
#runNumbers = [5827,5829,5830,5831]
runNumbers = np.load("/nfs/slac/g/exo/shaolei/make_run_list/phase2_Ra.npy")
#runNumbers = [r.GetRunNumber() for r in ProcDataSet]
''' 
Find more 
'''
#runNumbers.append(4770)
#runNumbers.append(4770)
#runNumbers.append(4772)
#runNumbers.append(4773)
#runNumbers.append(4997)
#runNumbers.append(5003)
'''
runNumbers.append(5008)
runNumbers.append(5020)
runNumbers.append(5021)
runNumbers.append(5027)
runNumbers.append(5030)
runNumbers.append(5033)
runNumbers.append(5036)
runNumbers.append(5042)
runNumbers.append(5051)
runNumbers.append(5052)
runNumbers.append(5053)
runNumbers.append(5056)
runNumbers.append(5057)
runNumbers.append(5064)
runNumbers.append(5067)
runNumbers.append(5069)
runNumbers.append(5118)

runNumbers.append(5322)
runNumbers.append(5323)
runNumbers.append(5325)
runNumbers.append(5326)
runNumbers.append(5396)

runNumbers.append(5794)
runNumbers.append(5795)
runNumbers.append(5818)
runNumbers.append(5851)
runNumbers.append(5852)
runNumbers.append(5853)
runNumbers.append(5854)
runNumbers.append(5855)
runNumbers.append(5856)
runNumbers.append(5857)
runNumbers.append(5859)
runNumbers.append(5860)
runNumbers.append(5861)
#runNumbers.append(5862)
#runNumbers.append(5872)
#runNumbers.append(6045)
runNumbers.append(5066)
runNumbers.append(5806)
runNumbers.append(5807)
runNumbers.append(5809)
runNumbers.append(5827)
runNumbers.append(5828)
runNumbers.append(5829)
runNumbers.append(5830)
# S5: P4_px ( 25.4, 0.0, 0.0)
runNumbers.append(5042)
'''
# S11: P4_py ( 0.0, 25.4, 0.0)
# S2: P2_nz ( 0.0, 0.0, -30.4)
# S8: P2_pz ( 0.0, 0.0, 30.4)
# S17: P4_ny ( 0.0, -25.4, 0.0)
'''
runNumbers.append(5843)
runNumbers.append(5851)
runNumbers.append(5852)
runNumbers.append(5853)
runNumbers.append(5854)
runNumbers.append(5855)
runNumbers.append(5856)
runNumbers.append(5857)
#S14+10cm
runNumbers.append(5838)

runNumbers.append(5842)
'''

'''
runNumbers.append(5842)
runNumbers.append(5843)
runNumbers.append(5851)
runNumbers.append(5852)
runNumbers.append(5853)
runNumbers.append(5854)
runNumbers.append(5855)
runNumbers.append(5856)
runNumbers.append(5857)
runNumbers.append(5859)
runNumbers.append(5863)
'''
# Only Th-228
'''
runNumbers.append(5003)
runNumbers.append(5008)
runNumbers.append(5020)
runNumbers.append(5021)
runNumbers.append(5027)
runNumbers.append(5030)
runNumbers.append(5033)
runNumbers.append(5036)
runNumbers.append(5042)
runNumbers.append(5051)
runNumbers.append(5052)
runNumbers.append(5053)
runNumbers.append(5056)
runNumbers.append(5057)
runNumbers.append(5118)
runNumbers.append(5474)
runNumbers.append(5535)

runNumbers.append(5827)
runNumbers.append(5828)
runNumbers.append(5829)
runNumbers.append(5830)
runNumbers.append(5851)
runNumbers.append(5852)
runNumbers.append(5853)
runNumbers.append(5854)
runNumbers.append(5855)
runNumbers.append(5856)
runNumbers.append(5857)
runNumbers.append(5859)
runNumbers.append(5860)
runNumbers.append(5861)
'''
#runNumbers.append(5787)
#runNumbers.append(5651)
# Co 
'''
runNumbers.append(5825)
runNumbers.append(5824)
runNumbers.append(5371)
runNumbers.append(5370)
runNumbers.append(5349)
runNumbers.append(5348)
runNumbers.append(5347)
runNumbers.append(5346)
runNumbers.append(5345)
runNumbers.append(5344)
runNumbers.append(5342)
runNumbers.append(5341)
runNumbers.append(5069)
runNumbers.append(5068)
runNumbers.append(5067)
runNumbers.append(5066)
runNumbers.append(5064)
runNumbers.append(5063)
runNumbers.append(5062)
runNumbers.append(4790)
runNumbers.append(4789)
runNumbers.append(4788)
runNumbers.append(4787)
runNumbers.append(4786)
runNumbers.append(4785)
'''
'''
# Cs
runNumbers.append(5822)
runNumbers.append(5820)
runNumbers.append(5339)
runNumbers.append(5338)
runNumbers.append(5047)
runNumbers.append(5074)
runNumbers.append(5073)
runNumbers.append(5072)
runNumbers.append(4781)
runNumbers.append(4780)
runNumbers.append(4779)
runNumbers.append(4778)
runNumbers.append(4777)
'''

# Ra 
'''
runNumbers.append(5818)
runNumbers.append(5817)
runNumbers.append(5816)
runNumbers.append(5815)
runNumbers.append(5814)
runNumbers.append(5813)
runNumbers.append(5812)
runNumbers.append(5811)
runNumbers.append(5810)
runNumbers.append(5809)
runNumbers.append(5807)
runNumbers.append(5806)
runNumbers.append(5805)
runNumbers.append(5804)
runNumbers.append(5803)
runNumbers.append(5802)
runNumbers.append(5801)
runNumbers.append(5800)
runNumbers.append(5799)
runNumbers.append(5798)
runNumbers.append(5797)
runNumbers.append(5796)
runNumbers.append(5795)
runNumbers.append(5794)
'''
# Phase 2
'''
runNumbers.append(7123)
runNumbers.append(7124)
runNumbers.append(7125)
runNumbers.append(7126)
runNumbers.append(7127)
runNumbers.append(7668)
runNumbers.append(7662)
runNumbers.append(7830)
runNumbers.append(7842)
'''


#infoRuns.CutDoubleComparison('RunNumber',5003,True)
#infoRuns.CutDoubleComparison('RunNumber',5020,False)
#infoRuns.CutDefaultRuns()

body = """
source /nfs/slac/g/exo_data4/users/maweber/software/Devel/setup.sh;
cd /nfs/slac/g/exo/shaolei/GAN_trainset/;
python PullDataForAPDStudyWithWF.py --RunNumber %s --energyThreshold 800.0 --outDir /nfs/slac/g/exo_data8/exo_data/users/shaolei/train_data/phase2/Ra/ --calib0 %f --calib1 %f --rotationAngle 0.5312 --subtractBaseline > %s 2> %s;
"""

allRuns = infoRuns.GetListOf('RunNumber')
#runNumbers = [int(run) for run in allRuns if int(run) < 3000]

runs = set([])
for i in range(allRuns.size()):
	runs.add(allRuns.at(i))
#runNumbers = [int(run) for run in runs if int(run) < 5522 and int(run) > 5422]
calib = ROOT.TTree()
calib.ReadFile('phase1_calibPars_ionization.txt')

applyCalibration = False#True

outDir = '/nfs/slac/g/exo/shaolei/GAN_trainset/output/'
for run in sorted(runNumbers):
	'''
	info = infoRuns.Clone()
	info.CutExact('RunNumber','%s'%run)
	week = info.GetListOf('WeekIndex')[0]
	calib.Draw('p0:p1','week == %s && multiplicity == 1'%week,'goff')
	'''
	calibP0 = 0.0
	calibP1 = 1.0
	if applyCalibration:
		calibP0 = calib.GetV1()[0]
		calibP1 = calib.GetV2()[0]
	print('calibP0',calibP0,'calibP1',calibP1)
	
	filename = '%srun_%s.sh'%(outDir,run)
	f = open(filename,'w')
	f.write(body % (run, calibP0, calibP1, filename.replace('.sh','.out'), filename.replace('.sh','.err')))
	f.close()
	cmd = 'chmod 755 %s'%filename
	os.system(cmd)
	cmd = 'bsub -R rhel60 -W 72:00 -o output/%s.out %s'%(run,filename)
	print cmd
	os.system(cmd)
	
