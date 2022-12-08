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
ap.add_argument("-c", "--monitorelement", required=True,
   help="monitor element to be analized")
ap.add_argument("-d", "--csvfilenametesting", required=True,
   help="csv to be tested")
ap.add_argument("-e", "--modeb", required=True,
   help="type of csv, 0 or 1")
ap.add_argument("-f", "--firstlumifortrain", required=True,
   help="first lumisection for training")
ap.add_argument("-g", "--lastlumifortrain", required=True,
   help="last lumisection for training")
ap.add_argument("-i", "--threshold", required=True,
   help="threshold")
args = vars(ap.parse_args())

key=args['monitorelement']
mode=int(args['mode'])
modeb=int(args['modeb'])
first=int(args['firstlumifortrain'])
last=int(args['lastlumifortrain'])
m=float(args['threshold'])



traindataset=str(args['csvfilenametraining'])
testdataset=str(args['csvfilenametesting'])

df_train, binstrain=u.loadcsv(traindataset,key,mode,first,last)
df_test, binstest=u.loadcsv(testdataset,key,modeb,0,99999)
   
train_data=u.preprocessing(binstrain)
test_data=u.preprocessing(binstest)

mse=u.training(train_data,test_data)


percentiles=[90,95,99,99.9]
if m not in percentiles:
    bisect.insort(percentiles, m)
toplot=[]
for a in percentiles:
    anom, anomal=u.threshold_for_anom_2(mse,df_test, modeb, a)
    print('\n Possible anomalies (',a,'th percentile) in lumisections: ',anomal)
    toplot.append(anom[0])
    
figure(figsize=(15, 10), dpi=80)
for i in range(len(toplot)):
    plt.axvline(x=toplot[i],color='r', linewidth=2,linestyle='--',label='1st anomaly at '+str(percentiles[i])+'th percentile')
plt.plot(mse,linewidth=2)

plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.xlabel("Loss",loc='right',fontsize=18)
plt.ylabel("a.u.",loc='top',fontsize=18)
plt.yticks(fontsize=14)
plt.figtext(0.13,0.887,'MSE',fontsize=18,fontweight='bold')
plt.title('Run '+str(testdataset)[-10:-4]+'  Monitor element: '+str(key),loc='left',fontsize=18,fontstyle='italic',x=0.066)
plt.savefig('plots/plot_'+str(testdataset)[-10:-4]+'_'+str(key)+'.pdf')