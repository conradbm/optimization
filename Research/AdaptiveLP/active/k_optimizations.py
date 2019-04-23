# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:04:11 2019

@author: bmccs
"""

from simulation_lp import get_optimization
import numpy as np
np.set_printoptions(suppress=True)

def get_k_optimizations(num_optimizers=50, data_shape=(10,5), batch_size=5, verbose=False, data=None):


    if verbose:
        print("Simulating synthetic data")
    Wijk=np.empty((data_shape[0], data_shape[1], num_optimizers))
    moves_ijk=[]
    for i in range(num_optimizers):
        if verbose:
            print("Optimizer {}".format(i))
        W, W_move_sequence=get_optimization(data=data, batch_size=batch_size, data_shape=data_shape, verbose=verbose)
        Wijk[:,:,i]=W
        moves_ijk.append(W_move_sequence)
        
    #A=np.average(W_ijk, axis=2)
    #A_move_sequence=np.argmax(A, axis=0)
    
    #if verbose:
    #    print("Wijk.shape {}".format(W_ijk.shape))
    #    print("A average {}".format(A))
    #    print("A move sequence {}".format(A_move_sequence))

    return Wijk, moves_ijk

#wijk,_=get_k_optimizations(data=None, num_optimizers=3, data_shape=(10,5), batch_size=10, verbose=True)
#print(wijk)
#print(_)