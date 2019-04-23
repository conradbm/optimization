# -*- coding: utf-8 -*-
"""
IMSE 882 Final Project
Traveling Salesman Heuristic
Find the shortest path from NFL Stadium 0 back to itself.
Heuristic -> Nearest Neighbor
Starting from an arbitrarily chosen initial city,
repeatedly choose for the next city the unvisited city closest to the
current one. Once all cities have been chosen, close the tour by returning
to the initial city.
@author: Blake Conrad
"""


import pandas as pd
import numpy as np
import random

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

# Display data


def printData(mat):
    for rowIndex in range(matrix.shape[0]):
        for colIndex in range(matrix.shape[1]):
            print("from {} to {} distance {}".format(rowIndex, colIndex, mat[rowIndex, colIndex]))
#printData(matrix)
            
def getRandomCity(mat):
    return random.randint(0, mat.shape[0]-1)
#getRandomCity(matrix)


def getRandomPath(mat, verbose=False):
    touched_cities=[]
    touched_cities.append(0)
    costs=[]
    for colIndex in range(1,matrix.shape[1]-1):
        nextCity=getRandomCity(matrix)
        while nextCity in touched_cities:
            nextCity=getRandomCity(matrix)
        
        touched_cities.append(nextCity)
        cost=mat[touched_cities[-2],touched_cities[-1]]
        costs.append(cost)

    touched_cities.append(0)
    cost=mat[touched_cities[-2],touched_cities[-1]]
    costs.append(cost)
    if verbose:
        print("Paths {}".format(touched_cities))
        print("Costs {}".format(costs))
        print("Total cost {}".format(sum(costs)))
    return touched_cities, costs, sum(costs)
 #path, costs, z=getRandomPath(matrix)  


def createKPaths(mat, K=1000000, verbose=False):
    
    simulate_df = pd.DataFrame()
    zscores=[]
    for i in range(K):
        path, costs, z = getRandomPath(mat)
        zscores.append(z)
        tmp = pd.DataFrame(path).transpose()
        simulate_df = pd.concat([simulate_df, tmp])
    simulate_df["z"]=zscores
    if verbose:
        print("Simulated dataset")
        print(simulate_df)
    return simulate_df 
#sdf=createKPaths(matrix)
#sdf.to_csv("simulated_paths.csv", index=False)
    
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

