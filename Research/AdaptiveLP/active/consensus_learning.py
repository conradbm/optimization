# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:20:09 2019

@author: bmccs
"""

from madm_concensus import get_madm_concensus
from k_optimizations import get_k_optimizations
import numpy as np


results=[]
for i in range(10):
    # Get K-optimizations from simulated data
    Wijk,_=get_k_optimizations(num_optimizers=20, data_shape=(10,5), batch_size=10)
    # Get our ranking
    rij,_=get_madm_concensus(Wijk=Wijk, policy=np.average)
    
    # optimized error
    c=1
    Wij_hat = np.average(Wijk, axis=2) - (c/2)*rij
    Wij_hat_move_sequence = np.argmax(Wij_hat, axis=0)
    results.append(Wij_hat_move_sequence)
    print(Wij_hat)
    print(Wij_hat_move_sequence)

print(results)

""" 
Output from 10 different datasets on the same distribution:

Test (1)
[array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64),
 array([5, 6, 5, 6, 0], dtype=int64)]

Test (2)
[array([2, 5, 0, 2, 0], dtype=int64),
 array([0, 3, 0, 4, 2], dtype=int64),
 array([7, 0, 4, 5, 2], dtype=int64),
 array([6, 4, 3, 1, 1], dtype=int64),
 array([0, 3, 3, 2, 1], dtype=int64),
 array([2, 5, 2, 2, 4], dtype=int64),
 array([0, 2, 0, 2, 2], dtype=int64),
 array([0, 2, 1, 4, 2], dtype=int64),
 array([9, 8, 8, 9, 9], dtype=int64),
 array([9, 8, 8, 9, 9], dtype=int64)]
"""
