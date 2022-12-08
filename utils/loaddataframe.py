import pandas as pd
import numpy as np




def readkeys(csv):
    df=pd.read_csv(csv,names=range(15))
    keys=set(df[2])
    return keys



    
def loadcsv(csv,key,mode,first,last):
    
    df=pd.read_csv(csv,names=range(15))
    

    
    if mode==0:
        keys=set(df[2])
        if key in keys:
            df_q=df.loc[df[2] == key]
            df_s=df_q.sort_values(by=[1],ignore_index=True)
            df_bins=df_s[7].str.extractall('(\d+)')[0].unstack()
            
            df_bins = df_bins.loc[first:last,:]
            df_bins=df_bins.reset_index(drop=True)
        else:
            print('Monitoring element is absent')

    elif mode==1:
        df=df.drop([0])
        df[8] = df[8].astype(int)
        df_s=df.sort_values(by=[8],ignore_index=True)
        df_bins=df_s[10].str.extractall('(\d+)')[0].unstack()
        df_bins=df_bins.reset_index(drop=True)
    return df_s, df_bins