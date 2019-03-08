# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:36:13 2019

@author: bmccs

Maximize sum_j{w_j*sum_i{data_ij}}
s.t.{
     sum_j{w_j}=1
     w_j >= 0 for all j

}
"""

import numpy as np
from scipy.optimize import minimize

data=np.random.randn(3,3)
print("Random data: {}".format(data))
print("Row sums: {}".format(np.sum(data, axis=0)))

def f(x):
    return -np.sum([x[i]*np.sum(data[:,i]) for i in range(len(data))])

eq_cons = {'type': 'eq',
           'fun' : lambda x: np.array([sum(x)-1])}       # sum(wj)=1 // normalize weights
ineq_cons = {'type': 'ineq',
             'fun' : lambda x: np.array([w for w in x])} # wj >= 0 // only positive weights

x0=np.random.randn(3)
print("Random starting point: {}".format(x0))

res = minimize(f, x0,
               constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9, 'disp': True})

print("Decision variables {} and sum(x)={}".format(res.x, sum(res.x)))