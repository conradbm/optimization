# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:03:08 2020

@author: blakeconrad
"""

from scipy.optimize import linprog

b = [-24, -34, -23]
c = [19, 18, 16, 22, 15, 17]
A = [[-4, -5, -6, -10, -6, -2],
      [-9, -7, -11, -8, -6, -7],
      [-8, -3, -7, -4, -3, -8]]
data = {"A":A, "b":b, "c":c}

x_bounds = [(0, 1) for i in range(len(data["c"]))]
x_bounds[1] = (0,0)
x_bounds[3] = (1,1)
x_bounds[4] = (1,1)
from scipy.optimize import linprog
res = linprog(data["c"], A_ub=data["A"], b_ub=data["b"], bounds=x_bounds)
print(res)