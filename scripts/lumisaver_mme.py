import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import argparse
import bisect
import utils as u
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--csvfilenametraining", required=True,
   help="csv input file for training")
ap.add_argument("-b", "--mode", required=True,
   help="type of csv, 0 or 1")
ap.add_argument("-c", "--csvfilenametesting", required=True,
   help="csv to be tested")
ap.add_argument("-d", "--modeb", required=True,
   help="type of csv, 0 or 1")
ap.add_argument("-e", "--monitorelement", required=False,
   help="monitor element to be analized (optional)")
ap.add_argument("-f", "--firstlumifortrain", required=False, default=0,
   help="first lumisection for training (optional)")
ap.add_argument("-g", "--lastlumifortrain", required=False, default=99999,
   help="last lumisection for training (optional)")
ap.add_argument("-i", "--firstlumifortest", required=False, default=0,
   help="first lumisection for testing (optional)")
ap.add_argument("-j", "--lastlumifortest", required=False, default=99999,
   help="last lumisection for testing (optional)")
ap.add_argument("-k", "--threshold", required=False, default=99.,
   help="threshold (optional)")
args = vars(ap.parse_args())

keyfromuser=args['monitorelement']
mode=int(args['mode'])
modeb=int(args['modeb'])
firsttrain=int(args['firstlumifortrain'])
lasttrain=int(args['lastlumifortrain'])
firsttest=int(args['firstlumifortest'])
lasttest=int(args['lastlumifortest'])
m=float(args['threshold'])

traindataset='runs/'+str(args['csvfilenametraining'])
testdataset='runs/'+str(args['csvfilenametesting'])

keys_train=u.readkeys(traindataset)
keys_test=u.readkeys(testdataset)

if keyfromuser:
    keys=[keyfromuser]
else:
    keys = keys_train.intersection(keys_test)

for key in keys:
    df_train, binstrain=u.loadcsv(traindataset,key,mode,firsttrain,lasttrain)
    df_test, binstest=u.loadcsv(testdataset,key,modeb,firsttest,lasttest)

    train_data=u.preprocessing(binstrain)
    test_data=u.preprocessing(binstest)
    print('\n--> Monitor element: ',key)
    mse=u.training(train_data,test_data)

    percentiles=[90., 95., 99., 99.9]
    if m not in percentiles:
        bisect.insort(percentiles, m)
        
    toplot=[]
    with open('logs/log_'+str(testdataset)[-10:-4]+'_'+str(key)+'.txt', 'w') as f:
        sys.stdout = f
        for a in percentiles:
            anom, anomal=u.threshold_for_anom_2(mse,df_test, modeb, a)
            print('\n Possible anomalies (',a,'th percentile) in lumisections: ',anomal)
            if anom.size:
                toplot.append(anom[0])
            
    figure(figsize=(15, 10), dpi=80)
    for i in range(len(toplot)):
        plt.axvline(x=toplot[i],color=plt.cm.hsv(i/len(percentiles)), linewidth=2,linestyle='--',label='1st anomaly at '+str(percentiles[i])+'th percentile')
    plt.plot(mse,linewidth=2)

    plt.legend(fontsize=14)
    plt.xticks(fontsize=14)
    plt.xlabel("MSE",loc='right',fontsize=18)
    plt.ylabel("a.u.",loc='top',fontsize=18)
    plt.yticks(fontsize=14)
    #plt.figtext(0.13,0.887,'MSE',fontsize=18,fontweight='bold')
    plt.title('Run '+str(testdataset)[-10:-4]+'  Monitor element: '+str(key),loc='left',fontsize=18,fontstyle='italic')
    plt.savefig('plots/mme_plot_'+str(testdataset)[-10:-4]+'_'+str(key)+'.pdf')
sys.stdout = sys.__stdout__
print("\n--> Results are in /logs and /plots folders")
    