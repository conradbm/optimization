# -*- coding: utf-8 -*-
"""
Sample LP from Tutorial.

@author: blakeconrad
"""

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
from scipy.optimize import linprog
res = linprog(c, 
              A_ub=A,
              b_ub=b,
              bounds=(x0_bounds, x1_bounds),
              options={"disp": True})
print(res)