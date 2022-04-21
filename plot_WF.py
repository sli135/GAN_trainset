###########################################################
#
# python plot_WF.py --ReadFile APDWF_newcut_Train.csv --nEvents 1000
#
###########################################################
import numpy as np 
import matplotlib as mpl
mpl.use('Agg') 
import matplotlib.pyplot as plt 
import csv
import argparse
def read_data(filename,nEvents):
    nLabels = 4
    nFeatures = 74*350

    features = []
    labels = []
    count = 0
    with open(filename) as infile:
        for line in infile:
            x = np.fromstring(line, dtype=float, sep=',')
            features.append(x[0:nFeatures])
            labels.append(x[nFeatures:nFeatures+4])

            count += 1
            if count >= nEvents:
                break
    print(filename + " has %i events" % count)
    return np.array(features), np.array(labels)
def plotWF(wf,label,ID):
    try:
        wf = wf.reshape(74,350)
    except:
        print "Not good shape: " + str(wf.shape)
        return 0
    title = "x = %.2f cm,y = %.2f cm,z = %.2f cm,e charge = %.2f keV" % (label[0],label[1],label[2],label[3])
    for i,signal in enumerate(wf):
        plt.plot(signal + 10 * i)
    plt.xlabel(r"t [$\mu$s]")
    plt.ylabel("channel number + a.u.")
    plt.title(title)
    plt.savefig("./pics/trainset_WF_%i.png"%ID,bbox_inches = 'tight')
    plt.show()
    plt.close()
def plotlabel(labels):
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.hist(labels[:,0], np.linspace(-200,200,40), histtype='step', color='b')
    ax2.hist(labels[:,1], np.linspace(-200,200,40), histtype='step', color='b')
    ax3.hist(labels[:,2], np.linspace(-200,200,40), histtype='step', color='b')
    ax4.hist(labels[:,3], np.linspace(500,3500,40), histtype='step', color='b')
    ax1.set_xlim([-200, 200])
    ax1.set_ylim(ymin=0)
    ax2.set_xlim([-200, 200])
    ax2.set_ylim(ymin=0)
    ax3.set_xlim([-200, 200])
    ax3.set_ylim(ymin=0)
    ax4.set_xlim([500, 3500])
    ax4.set_ylim(ymin=0)

    ax1.set_xlabel('x (cm)')
    ax2.set_xlabel('y (cm)')
    ax3.set_xlabel('z (cm)')
    ax4.set_xlabel('charge energy (keV)')
    plt.savefig("./pics/trainset.png",bbox_inches = 'tight')
    plt.show()
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ReadFile', type=str)
    parser.add_argument('--nEvents', type=int)
    args = parser.parse_args()
    filename = args.ReadFile
    nEvents = args.nEvents
    filepath = "/nfs/slac/g/exo-userdata/users/shaolei/data_reweight/"
    X,Y = read_data(filepath + filename,nEvents)
    print X.shape,Y.shape
    plotlabel(Y)
    for i in range(20):
        if Y[i][3] > 1000: plotWF(X[i],Y[i],i)