# -*- coding: utf-8 -*-
"""
Basic LP Template!

@author: blakeconrad
"""
import numpy as np

ROWS = 5
COLS = 5
c = [np.random.exponential() for j in range(COLS)]
A = np.abs(np.random.randn(ROWS,COLS)).tolist()
b = [np.random.chisquare(5) for j in range(ROWS)]
x_bounds = [(0, None) for j in range(COLS)]

from scipy.optimize import linprog
res = linprog(c, 
              A_eq=A,
              b_eq=b,
              bounds=x_bounds,
              options={"disp": True})

print("A")
print(np.matrix(A))
print("b")
print(b)
print("c")
print(c)
print("result")
print(res)

# Interpretation
# If we had to select an xj to increase the values of resource j to,
#  to meet our constraints, we should increase x[0] and x[5].
