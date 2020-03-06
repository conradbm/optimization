# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:05:49 2020

@author: blakeconrad
"""

import pandas as pd
import numpy as np

df = pd.read_csv("DraftKingsdata_Cleaner.csv")

import os
import pyomo.environ as pyo
from pyomo.environ import *

from pyomo.opt import SolverFactory

opt = pyo.SolverFactory('glpk')

model = ConcreteModel()

Names = df.Name.tolist()
Salaries = df.Salary.tolist()
AvgPoints = df.AvgPointsPerGame.tolist()
P = df.iloc[:,-5:].values
budget = 50000

N = len(Names)
model.x = Var(range(N),
               within=Binary)
model.g1 = Var(within=Binary)
model.h1 = Var(within=Binary)

model.obj = Objective(expr = pyo.summation(AvgPoints, model.x), 
                      sense=maximize)

#import pyomo.environ as aml
model.constraints = ConstraintList()

# Valid team/player constraints
model.constraints.add(pyo.summation(model.x) == 8)

model.constraints.add( (1+model.g1) <= pyo.summation(P[:,4].tolist(),model.x) ) #PG
model.constraints.add(pyo.summation(P[:,4].tolist(),model.x)<=(2+model.g1))

model.constraints.add( (1+(1-model.g1)) <= pyo.summation(P[:,0].tolist(),model.x) ) #SG
model.constraints.add(pyo.summation(P[:,0].tolist(),model.x)<=(2+(1-model.g1)))

model.constraints.add( (1+model.h1) <= pyo.summation(P[:,2].tolist(),model.x) ) #SF
model.constraints.add(pyo.summation(P[:,2].tolist(),model.x)<=(2+model.h1))

model.constraints.add( (1+(1-model.h1)) <= pyo.summation(P[:,3].tolist(),model.x)) #PF
model.constraints.add(pyo.summation(P[:,3].tolist(),model.x)<=(2+(1-model.h1)))

model.constraints.add( 1<= pyo.summation(P[:,1].tolist(),model.x)) #C
model.constraints.add(pyo.summation(P[:,1].tolist(),model.x)<=2)

# Salary/budget
model.constraints.add( pyo.summation(Salaries,model.x)<=budget )

# Create a model instance and optimize
instance = model.create_instance()
results = opt.solve(instance, tee=True)
instance.display()
instance.x.display()
instance.obj.display()
from itertools import compress
x = list(map(lambda x: bool(x), list(instance.x.get_values().values())))
g = instance.g1.get_values().values()
h = instance.h1.get_values().values()

print("="*20)
print("Your Final Fantacy Team")
print(df[x][["Position", "Name", "Salary", "AvgPointsPerGame"]])
print("="*20)
