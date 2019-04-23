# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:20:09 2019

@author: bmccs
"""
import pandas as pd
import os
print(os.getcwd())
print(os.listdir())
from madm_concensus import get_madm_concensus
from k_optimizations import get_k_optimizations
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

data=pd.read_csv("clean_data.csv")
print(data)
input("...")
results=[]
for i in range(10):
    print("Epoch {}".format(i))
    # Get K-optimizations from simulated data
    
    Wijk,_=get_k_optimizations(data=data,num_optimizers=10, data_shape=(10,5), batch_size=35, verbose=False)
    Wijk=np.nan_to_num(Wijk) #optimizer throws nan if it can't figure it out, replace with 0.
    if np.isnan(Wijk).any():
        break

    # Get our ranking
    print("Wijk {}".format(Wijk))
    print("Wijk_moves {}".format(_))
    
    rij,_=get_madm_concensus(Wijk=Wijk, policy=np.average, verbose=True)
    print("rij {}".format(rij))
    print("rij_moves {}".format(_))
    # optimized loss function penalized by madm rank
    c=1
    Wij_hat = np.average(Wijk, axis=2) - (c/2)*rij
    Wij_hat_move_sequence = np.argmax(Wij_hat, axis=1)
    results.append(Wij_hat_move_sequence)
    print("*******************")
    print("***** RESULTS *****")
    print("*******************")
    print("Wij_hat {}".format(Wij_hat) )
    print("Wij_hat_moves {}".format(results[-1]))


print(results)

""" 
Output from 10 different datasets on the same distribution:

Test (1)
[array([2, 2, 0, 0, 2, 3, 2, 1, 3, 4], dtype=int64),
 array([3, 2, 3, 4, 0, 2, 1, 0, 2, 3], dtype=int64),
 array([4, 4, 4, 0, 1, 1, 0, 4, 0, 0], dtype=int64),
 array([0, 2, 0, 2, 2, 0, 4, 0, 3, 1], dtype=int64),
 array([1, 4, 2, 0, 0, 2, 1, 4, 0, 0], dtype=int64),
 array([3, 0, 1, 0, 0, 3, 4, 3, 4, 3], dtype=int64),
 array([1, 4, 4, 1, 1, 2, 0, 1, 3, 1], dtype=int64),
 array([2, 0, 0, 2, 0, 3, 3, 2, 3, 3], dtype=int64),
 array([4, 4, 0, 1, 4, 2, 4, 1, 0, 2], dtype=int64),
 array([1, 4, 2, 0, 2, 4, 4, 3, 3, 0], dtype=int64)]
"""
