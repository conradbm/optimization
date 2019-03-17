# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:04:11 2019

@author: bmccs
"""

from simulation_lp import get_optimization
import numpy as np
np.set_printoptions(suppress=True)

def get_k_optimizations(num_optimizers=50, data_shape=(10,5), batch_size=5):


    print("Simulating synthetic data")
    W_ijk=np.empty((data_shape[0], data_shape[1], num_optimizers))
    moves_ijk=[]
    for i in range(1,num_optimizers):
        W, W_move_sequence=get_optimization(batch_size=batch_size, data_shape=data_shape)
        W_ijk[:,:,i]=W
        moves_ijk.append(W_move_sequence)
        
    A=np.average(W_ijk, axis=2)
    A_move_sequence=np.argmax(A, axis=0)
    print("Wijk.shape {}".format(W_ijk.shape))
    print("Wijk average {}".format(A))
    print("A move sequence {}".format(A_move_sequence))

    return W_ijk, W_move_sequence

#wijk,_=get_k_optimizations(data=None, K=100, DATA_SHAPE=(10,5), NUM_BATCHES=10)