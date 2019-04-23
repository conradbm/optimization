# -*- coding: utf-8 -*-
"""
IMSE 882 Final Project
Traveling Salesman Heuristic
Find the shortest path from NFL Stadium 0 back to itself.
@author: Blake Conrad
"""

import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)

from sklearn.linear_model import LinearRegression
sdf=pd.read_csv("simulated_paths.csv")
reg = LinearRegression(fit_intercept=False).fit(sdf.loc[:, sdf.columns != "z"],
                                                sdf.loc[:, sdf.columns == "z"])
coefs=np.array(reg.coef_[0], np.int8)
print(coefs)
import matplotlib.pyplot as plt
plt.plot(reg.coef_[0])