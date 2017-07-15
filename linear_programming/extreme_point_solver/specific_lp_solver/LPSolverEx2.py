### A Worked Example
###
###
from __future__ import division 
import numpy as np

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
xint1 = (lambda y:(y-1, y))
xint2 = (lambda y:(y/2, y))

###
### Constraint functions AND Y-intercept points -- i.e. hold x=0
###
y1 = (lambda x:(x, x+1))
y2 = (lambda x:(x, 2*x))

###
### Each (x,y) point in our domain for each constraint
###
points1=[y1(xi) for xi in x_domain]
points2=[y2(xi) for xi in x_domain]
points=[set(points1), set(points2)]
###
### Establish our critial points list
###
critical_points=[]
critical_points.append(y1(0))
critical_points.append(xint1(0))
critical_points.append(y2(0))
critical_points.append(xint2(0))

print "X-Y Intercepts: "
ls1 = set(critical_points)
print ls1
print "Other Extreme Points:"
ls2 = list(set.intersection(*points))
print ls2
