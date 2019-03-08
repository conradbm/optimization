###
### Author: Blake Conrad
### Contents: Explain and conceptualize the idea of the extreme or corner point
###           algorithm to solve a system of constraints for an objective function.
###
###
###
### The Problem
###
###
### max z0 = 2x + 3y
### s.t.
###     y <= 5x + 2
###     y <= -x + 5
###     y <= -3x + 1
###     x,y >= 0
###
###
###
### The Procedure
###
###
### 1. Define each constraint in terms of y=mx+b and x=my+b as functions (or lambdas) returning tuples ((x,y) points).
### 2. Define a range of x-input values (the bigger ypu go, the closer to optimal you can get)
### 3. Compile a list for every "tuple" points for each constraint.
### 4. Find all intersecting points in your lists of points for each equation
### 5. Append each of (4)'s intersection points to a list of each y-intersept and x-intercept of each constraint.
### 6. For each critial point in (5), determine which is the max in your objective function.
###
###
### A Worked Example
###
###
from __future__ import division 
import numpy as np
flatten = (lambda l: [item for sublist in l for item in sublist])

###
### Objective Function -- Returns a value
###
z0 = (lambda x,y: 2*x + 3*y)

###
### Your domain of X-Values
###
x_domain = np.arange(0,100, 1)

###
### X-Intercept points -- i.e. hold y=0
###
xint1 = (lambda y:(y/5 - 2/5, y))
xint2 = (lambda y:(-y + 5, y))
xint3 = (lambda y:(-y/3 + 1, y))
x_functions=[xint1, xint2, xint3]

###
### Constraint functions AND Y-intercept points -- i.e. hold x=0
###
y1 = (lambda x:(x, 5*x+2))
y2 = (lambda x:(x, -x+5))
y3 = (lambda x:(x, -3*x+1))
y_functions=[y1, y2, y3]

###
### Each (x,y) point in our domain for each constraint
###
points1=[y1(xi) for xi in x_domain]
points2=[y2(xi) for xi in x_domain]
points3=[y3(xi) for xi in x_domain]
points=[set(points1), set(points2), set(points3)]

###
### Establish our critial points list
###
critical_points=[]
x_y_intercepts=flatten([[f[0](0), f[1](0)] for f in zip(x_functions, y_functions)])
critical_points.append(x_y_intercepts)

print "X-Y Intercepts:"
print critical_points

###
### Append all critical points
###
intersection_points = list(set.intersection(*points))
critical_points.append(intersection_points)

###
### Remove empty lists from our list (If we found none above)
###
critical_points = filter(lambda x: len(x) > 0, critical_points)
critical_points = flatten(critical_points)
print "All Extreme Points: "
print critical_points

print "Max Solution:",
values = [z0(p[0], p[1])  for p in critical_points]
print max(values)
