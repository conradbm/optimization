# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:51:06 2019

@author: bmccs
"""

import pandas as pd
import numpy as np
def readData(fileName):
    import os
    
    os.chdir("C:\\Users\\bmccs\\Desktop\\optimization\\882\\heuristic")
    # Read in data
    df = pd.read_csv(fileName)
    matrix=df.iloc[:,1:].as_matrix()
    return matrix
matrix=readData("Nfldata.csv")


def nearestNeighborHeiristic(mat):
    touched_cities=[]
    touched_cities.append(0)
    costs=[]
    while len(touched_cities) != mat.shape[0]-1: #visit every city
        #j=np.argmin(mat[touched_cities[-1],:])
        options=[]
        optionsCost=[]
        for col in range(mat.shape[1]):
            if col not in touched_cities:
                options.append(col)
                optionsCost.append(mat[touched_cities[-1],col])
        j=np.argmin(optionsCost)
        c=mat[touched_cities[-1],options[j]]
        touched_cities.append(options[j])
        costs.append(c)
        print("From {} To {} With Cost {}".format(touched_cities[-2], touched_cities[-1], c))
    touched_cities.append(0)
    costs.append(mat[touched_cities[-2], touched_cities[-1]]) 
    print("From {} To {} With Cost {}".format(touched_cities[-2], touched_cities[-1], c))
    return touched_cities, costs

path, costs=nearestNeighborHeiristic(matrix)

print(path)
print(sum(costs))