import pandas as pd
import numpy as np


def preprocessing(bins):
    x_train=bins.to_numpy()
    x_train=np.array(x_train, dtype=np.float64)
    min_val = np.min(x_train,axis=0)
    max_val = np.max(x_train,axis=0)
    data_= np.divide(x_train, max_val - min_val, out=np.zeros_like(x_train), where=max_val - min_val!=0)
    #data_ = (x_train - min_val) / (max_val - min_val)
    #data_ = np.where(np.isnan(data_), 0, data_)
    data_=np.array(data_, dtype=np.float64)
    return data_