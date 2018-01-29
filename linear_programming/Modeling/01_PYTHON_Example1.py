# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog

from scipy.optimize import linprog
"""
Consider the following problem:

Minimize: f = -1*x[0] + 4*x[1]

Subject to: -3*x[0] + 1*x[1] <= 6

    1*x[0] + 2*x[1] <= 4
        x[1] >= -3


"""

c = [-1, 4]
A = [[-3, 1], # <=
     [1, 2]]  # <=
b = [6, 4]
x0_bounds = (None, None) # >=, <=
x1_bounds = (-3, None) # >=, <=

res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
              options={"disp": True})
res
res.x
