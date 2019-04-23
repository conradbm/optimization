# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:19:06 2019

@author: bmccs
"""
from k_optimizations import get_k_optimizations
from skcriteria import Data, MAX
from skcriteria.madm import closeness, simple
import pandas as pd
import numpy as np


def get_madm_concensus(Wijk=None, num_optimizers=100, data_shape=(10,5), batch_size=10, policy=np.average, verbose=False):
        
    # Get data from simulation
    if Wijk is None:
        Wijk, move_sequence = get_k_optimizations(num_optimizers=num_optimizers,
                                                  data_shape=data_shape,
                                                  batch_size=batch_size, 
                                                  verbose=verbose)
    
    # Construct alternative-space
    alternatives={}
    alternative_num=0
    for i in range(Wijk[:,:,0].shape[0]):
        for j in range(Wijk[:,:,0].shape[1]):
            alternatives[alternative_num]=(i,j)
            alternative_num+=1
    #print(alternatives)
    
    # Construct decision-matrix
    DM=np.empty((alternative_num,Wijk.shape[2]))
    for a,loc in alternatives.items():
        for k in range(Wijk.shape[2]):
            DM[a,k]=Wijk[loc[0],loc[1],k]
    #print(DM)
    
    # Putting it all together
    alternative_names = [v for k,v in alternatives.items()]
    criterion_names = [k for k in range(Wijk.shape[2])]
    criteria = [MAX for i in criterion_names]
    weights = [1/len(criterion_names) for i in range(len(criterion_names))]
    df = pd.DataFrame(DM,
                      index=alternative_names,
                      columns=criterion_names)
     
    if verbose:
        print("Alternatives {}".format(alternative_names))
        print("Criteria {}".format(criterion_names))
        print("Weights {}".format(weights))
        print("Decision Matrix {}".format(df))
    
    
    # Execute MADM
    data = Data(df.as_matrix(),
                criteria,
                weights,
                anames=df.index.tolist(),
                cnames=df.columns
                )
    
    # Execute on 3 decision makers
    dm1 = simple.WeightedSum()
    dm2 = simple.WeightedProduct()
    dm3 = closeness.TOPSIS()
    dec1 = dm1.decide(data)
    dec2 = dm2.decide(data)
    dec3 = dm3.decide(data)
    
    ranks=[dec1.rank_, dec2.rank_,dec3.rank_]
    results = pd.DataFrame({"TOPSIS":dec3.rank_,
                            "WeightedSum":dec1.rank_,
                            "WeightedProduct":dec2.rank_},
                            index=df.index.tolist())
    
    if verbose:
        print("MADM Results: {}".format(results))
    concensus_results=pd.DataFrame({"ConsensusRank":policy(results, axis=1)},index=results.index)
    rij=concensus_results.as_matrix().reshape(Wijk.shape[0],Wijk.shape[1])
    rij_move_sequence=np.argmin(rij,axis=1)
    #if verbose:
    #    print("rij {}".format(rij))
    #    print("rij_move_sequence {}".format(rij_move_sequence))
    return rij, rij_move_sequence

#wijk,_=get_k_optimizations(data=None, num_optimizers=5, data_shape=(10,5), batch_size=5, verbose=True)

#rij, _=get_madm_concensus(Wijk=wijk, policy=np.average )
#print(rij)
#print(_)