# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:36:13 2019

@author: bmccs


}
"""

import numpy as np
from scipy.optimize import minimize

N=10
T=5
data=np.abs(np.random.randn(N,T))

def f(x):

    return -np.sum([data[i,j]*x.reshape(N,T)[i,j] for i in range(x.reshape(N,T).shape[0]) for j in range(x.reshape(N,T).shape[1])])

eq_cons = {'type': 'eq',
           'fun' : lambda x: np.array([np.sum(w)-1 for w in x.reshape(N,T).T])}       # sum_i(Wij)=1 for all j // normalize weight columns
ineq_cons = {'type': 'ineq',
             'fun' : lambda x: np.array([w for w in x])} # Wij >= 0 for all i,j // only positive weights

x0=np.random.randn(N,T)
print("Random starting point: {}".format(x0))

res = minimize(f, x0,
               constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9})

np.set_printoptions(suppress=True)
print("Results")
print(res.x.reshape(N,T))
print("Data")
print(data)