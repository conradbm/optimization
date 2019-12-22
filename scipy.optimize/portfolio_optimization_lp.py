# -*- coding: utf-8 -*-
"""
Simple portfolio optimization LP.

@author: blakeconrad
"""

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)
                    
# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ["AMZN", "MSFT", "GOOGL", "APPL", "BRK.A",
           "FB", "TCEHY", "BABA", "JNJ", "JPM"]

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2011-01-01'
end_date = '2019-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader(tickers, 'yahoo', start_date, end_date)

# Get value by aggregating percent change.
df_pc        = (panel_data.Close-panel_data.Close.shift(1))/panel_data.Close
df_pc = df_pc.fillna(0)
pc_matrix = df_pc.groupby(df_pc.index.year).sum()
cov_matrix   = df_pc.groupby(df_pc.index.year).cov()
corr_matrix = df_pc.groupby(df_pc.index.year).corr()
corr_matrix = corr_matrix.fillna(0)

# Convert to matrices
N = len(cov_matrix.index.get_level_values(0).unique())
M = len(tickers)
cov_matrix = cov_matrix.as_matrix().reshape(N,M,M)
corr_matrix = corr_matrix.as_matrix().reshape(N,M,M)
pc_matrix = pc_matrix.as_matrix()

# Optimize LP
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
import matplotlib.pyplot as plt
alpha=1
def f(x):
    # Optimize: Maximize. Expected Return - Risk - Correlation
    #               s.t.  Percent of each company allocated Sum = 1
    #                     No negative allocations.
    # (=>)
    #           Minimize. -Expected Return + Risk + Correlation.
    #
    # Normalize to make all three equally important.
    #
    #
    #total = pc_matrix.dot(x).sum() + cov_matrix.dot(x).sum() + corr_matrix.dot(x).sum()
    #return -alpha*(pc_matrix.dot(x).sum()/total) + (1-alpha)*((cov_matrix.dot(x).sum()/total) + (corr_matrix.dot(x).sum()/total))
    return pc_matrix.dot(x).sum()  #AMZN exploits max PC return
    #return cov_matrix.dot(x).sum() #MSFT and APPL minimize risk/volatility
    #return corr_matrix.dot(x).sum() #MSFT and APPL maximize diversification/correlation

DV_SZ = len(tickers)
x0=np.random.randn(DV_SZ)
x_bounds = [(0, None) for j in range(DV_SZ)]
A = [np.ones(DV_SZ)]
lb = [1]
ub = [1]
x_constraints = LinearConstraint(A, lb, ub)
results={}
for a in np.arange(0,1,0.1):
    print(a)
    res = minimize(f, x0, bounds=x_bounds, constraints=[x_constraints])
    results[a] = res.x

df_results=pd.DataFrame(results)
print(df_results)