import pandas as pd
import numpy as np

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def threshold_for_anom(data: np.array, m = 2.) -> list:
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    anom=np.where(s>m)[0]
    anomal=[]
    for i in range(anom.shape[0]):
        anomal.append(df_test[8][anom[i]])
    return anomal

def threshold_for_anom_2(data: np.array, df_test: pd.DataFrame, modeb, m = 99):
    d = np.percentile(data, m)
    anom=np.where(data>d)[0]
    anomal=[]
    if modeb==0:
        for i in range(anom.shape[0]):
            anomal.append(df_test[1][anom[i]])
    elif modeb==1:
        for i in range(anom.shape[0]):
            anomal.append(df_test[8][anom[i]])
    return anom, anomal

def threshold_for_anom_moving_average(data: np.array, df_test: pd.DataFrame, modeb, m = 99):
    data=moving_average(data, n=5)
    d = np.percentile(data, m)
    anom=np.where(data>d)[0]
    anomal=[]
    if modeb==0:
        for i in range(anom.shape[0]):
            anomal.append(df_test[1][anom[i]])
    elif (modeb==1 or modeb==2):
        for i in range(anom.shape[0]):
            anomal.append(df_test[8][anom[i]])

    return anom, anomal

