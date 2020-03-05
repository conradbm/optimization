# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:48:40 2020

@author: blakeconrad
"""
import os
os.environ["PATH"] += os.pathsep + r"C:\Users\blakeconrad\Documents\winglpk-4.65\glpk-4.65\w64"
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Create a solver
"""
    asl                  + Interface for solvers using the AMPL Solver
                           Library
    baron                  The BARON MINLP solver
    bilevel_blp_global   + Global solver for continuous bilevel linear
                           problems
    bilevel_blp_local    + Local solver for continuous bilevel linear
                           problems
    bilevel_bqp          + Global solver for bilevel quadratic
                           problems
    bilevel_ld           + Solver for bilevel problems using linear
                           duality
    cbc                    The CBC LP/MIP solver
    conopt                 The CONOPT NLP solver
    contrib.gjh            Interface to the AMPL GJH "solver"
    cplex                  The CPLEX LP/MIP solver
    cplex_direct           Direct python interface to CPLEX
    cplex_persistent       Persistent python interface to CPLEX
    gams                   The GAMS modeling language
    gdpbb                * Branch and Bound based GDP Solver
    gdpopt               * The GDPopt decomposition-based Generalized
                           Disjunctive Programming (GDP) solver
    glpk                 * The GLPK LP/MIP solver
    gurobi                 The GUROBI LP/MIP solver
    gurobi_direct          Direct python interface to Gurobi
    gurobi_persistent      Persistent python interface to Gurobi
    ipopt                  The Ipopt NLP solver
    mindtpy              * MindtPy: Mixed-Integer Nonlinear
                           Decomposition Toolbox in Pyomo
    mosek                  Direct python interface to Mosek
    mpec_minlp           + MPEC solver transforms to a MINLP
    mpec_nlp             + MPEC solver that optimizes a nonlinear
                           transformation
    multistart           * MultiStart solver for NLPs
    path                   Nonlinear MCP solver
    pico                   The PICO LP/MIP solver
    ps                   * Pyomo's simple pattern search optimizer
    py                   + Direct python solver interfaces
    scip                   The SCIP LP/MIP solver
    trustregion          * Trust region filter method for black
                           box/glass box optimization
    xpress                 The XPRESS LP/MIP solver
"""

opt = pyo.SolverFactory('glpk')

b = [24, 34, 23]
c = [19, 18, 16, 22, 15, 17]
A = [[4, 5, 6, 10, 6, 2],
      [9, 7, 11, 8, 6, 7],
      [8, 3, 7, 4, 3, 8]]

M = len(b)
N = len(c)

data = {"A":A, "b":b, "c":c}

model = ConcreteModel()

model.x = Var(range(N),
               within=Binary)

model.obj = Objective(expr = pyo.summation(c, model.x), 
                      sense=maximize)

model.constraints = ConstraintList()

for i in range(len(data["b"])):
    model.constraints.add( pyo.summation(A[i], model.x)<= b[i] )

# Create a model instance and optimize
instance = model.create_instance()
results = opt.solve(instance)
instance.display()
print ("\n===== results",i)
results = opt.solve(instance)
instance.display()