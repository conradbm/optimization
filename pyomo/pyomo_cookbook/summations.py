# -*- coding: utf-8 -*-
"""
Example 1. Simple Matrices
min. sum_j^n{c[j]*x[j]}
s.t. sum_j^n{a[i,j]*x[j]} >= b[j] for all j in {1..m}
"""

# abstract1.py
from __future__ import division
from pyomo.environ import *

model = AbstractModel()
model.m = Param(within=NonNegativeIntegers)
model.n = Param(within=NonNegativeIntegers)
model.I = RangeSet(1, model.m)
model.J = RangeSet(1, model.n)
model.a = Param(model.I, model.J)
model.b = Param(model.I)
model.c = Param(model.J)
# the next line declares a variable indexed by the set J
model.x = Var(model.J, domain=NonNegativeReals)

def obj_expression(model):
    return summation(model.c, model.x)
    #return sum([model.c[i,j]*model.x[i,j] for i in model.I for j in model.J])
model.OBJ = Objective(model.I, model.J, rule=obj_expression)

def ax_constraint_rule(model, i):
    # return the expression for the constraint for i
    return sum(model.a[i,j] * model.x[j] for j in model.J) >= model.b[i]
# the next line creates one constraint for each member of the set model.I
model.AxbConstraint = Constraint(model.I, rule=ax_constraint_rule)


"""
# data.dat
# one way to input the data in AMPL format
# for indexed parameters, the indexes are given before the value
param m := 1 ;
param n := 2 ;
param a :=
1 1 3
1 2 4
;
param c:=
1 2
2 3
;
param b := 1 1 ;

"""