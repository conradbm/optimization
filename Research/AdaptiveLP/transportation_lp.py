# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:36:13 2019

@author: bmccs


}
"""

import numpy as np
from scipy.optimize import minimize

N=4
T=3
cost=np.abs(np.random.randn(N,T))
capacity=np.array([20,15,10,10]) # <=
demand=np.array([20,10,15]) # >=
def f(x):
    return np.sum([cost[i,j]*x.reshape(N,T)[i,j] for i in range(x.reshape(N,T).shape[0]) for j in range(x.reshape(N,T).shape[1])])

eq_cons = {'type': 'eq',
           'fun' : lambda x: np.array([])}       # sum_i(Wij)=1 for all j // normalize weight columns
ineq_cons = {'type': 'ineq',
             'fun' : lambda x: np.array([np.sum(x.reshape(N,T)[:,j])-demand[j] for j in range(x.reshape(N,T).shape[1])] + 
                                         [-np.sum(x.reshape(N,T)[i,:])+capacity[i] for i in range(x.reshape(N,T).shape[0])] + 
                                         [w for w in x])} # Xij >= 0 for all i,j // only positive weights

x0=np.abs(np.random.randn(N,T))
print("Random starting point: {}".format(x0))

res = minimize(f, x0,
               constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9, 'disp': True})

np.set_printoptions(suppress=True)
print("Results\n")
print("Decision Variables")
print(res.x.reshape(N,T))
print("Costs")
print(cost)
print("Demand")
print(demand)
print("Capacity")
print(capacity.reshape(4,1))