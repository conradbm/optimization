# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:14:29 2019

@author: bmccs

LP Example
"""
from scipy.optimize import linprog
import numpy as np

c = np.random.randn(5,10)
Aeq = [[1 for i in range(10)]]
beq = [1]
bounds = tuple([(0,1) for i in range(10)])

res = linprog(c, A_eq=Aeq, b_eq=beq, bounds=bounds,
              options={"disp": True})



print(res)
