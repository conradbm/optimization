
# coding: utf-8

# In[1]:


# Libraries
from __future__ import division
import numpy as np


# In[4]:


# Helper Functions
#
#
# Function: golden_search
#
# Required Parameters:
# 1. x, a list containing a scalar in each dimension, x1, x2, ... , xN 
# 2. d, a list containing a direction in each dimension, d1, d2, ... , dN
#
# Optional Parameters:
# 1. low, a point to lower bound the initial golden search
# 2. high, a point to upper bound the initial golden search
# 3. alpha, the golden ratio number
# 4. verbose, to echo each steps progress
def golden_search(x, d, low=0, high=1, eps=0.1, alpha = 0.618, verbose=False):

    #min (x1-2)^4 +(x1-2x2)^2
    flambda = lambda l: ((x[0]-l*d[0])-2)**4 + ((x[0]-l*d[0])-2*((x[1]-l*d[1])))**2
    # min x1+x2+x3
    #flambda = lambda l: ((x[1]-l*d[1])) + ((x[1]-l*d[1])) + ((x[1]-l*d[1]))
    
    if verbose:
        print("*******************************")
        print("Executing Golden Ratio Search")
        print("*******************************")

    # Define Constants
    k=0
    
    # Create lists
    lam=list()
    mu=list()
    a=list()
    b=list()
    distances=list()
    
    # Step 1
    a.append(low)
    b.append(high)

    lam0 = a[k] + (1-alpha)*(b[k]-a[k])
    mu0 = a[k] + alpha*(b[k]-a[k])
    
    lam.append(lam0)
    mu.append(mu0)
    
    if verbose:
        print("************************")
        print(("[a,b]"), "|b[k]-a[k]|")
        print("************************")
        
    while True:
        distances.append(abs(b[k]-a[k])) 
        if verbose:
            print(a[k],b[k], distances[k])

        if(distances[k] < eps): # optimal soln lies within [a,b]
            break
        elif flambda(lam[k]) > flambda(mu[k]):
            # Step 2
            a.append(lam[k])
            b.append(b[k])
            lam.append(mu[k])
            mu.append(a[k+1] + alpha*(b[k+1]-a[k+1]))
        elif flambda(lam[k]) <= flambda(mu[k]):
            # Step3
            a.append(a[k])
            b.append(mu[k])
            mu.append(lam[k])
            lam.append(a[k+1]+(1-alpha)*(b[k+1]-a[k+1]))
        else:
            print("Something went wrong.")

        k += 1
    
    #return random.uniform(a[-1], b[-1])
    return (a[-1]+b[-1])/2


# In[5]:


# Simple Gradient Search for 2 variables using golden search
#min (x1-2)^4 +(x1-2x2)^2
f = lambda x1,x2: pow(x1-2,4)+pow(x1-2*x2, 2)
fgradient = lambda x1,x2: np.array([4*pow(x1-2,3)+2*(x1-2*x2),
                                    -4*(x1-2*x2)])

def printer(index):
    print("X:",xList[index], "D:",dList[index], "Z:",zList[index], "l:",lList[index])
    

# Inititialization Step
eps=0.01
x1=0
x2=3
z=f(x1,x2)
xList=[]
dList=[]
zList=[]
lList=[]
d1=fgradient(x1,x2)[0]
d2=fgradient(x1,x2)[1]

xList.append((x1,x2))
dList.append((d1,d2))
zList.append(z)
lList.append("nil")

# Main Step
while np.linalg.norm(fgradient(xList[-1][0],xList[-1][1])) >= eps:
    
    # Display progress
    printer(-1)
    
    # Calculate optimal lambda
    lambd= golden_search(xList[-1], dList[-1],verbose=False)
    
    # Update position
    x1=xList[-1][0]-lambd*dList[-1][0]
    x2=xList[-1][1]-lambd*dList[-1][1]
    z=f(x1,x2)
    
    # Update direction
    d1=fgradient(x1,x2)[0]
    d2=fgradient(x1,x2)[1]
    
    # Store information for printer
    xList.append((x1,x2))
    dList.append((d1,d2))
    zList.append(z)
    lList.append(lambd)

print("Final Solution")
printer(-1)


# In[7]:


# Conjugate Gradient Method of Fletcher and Reeves p. 423

f = lambda x1,x2: pow(x1-2,4)+pow(x1-2*x2, 2)
fgradient = lambda x1,x2: np.array([4*pow(x1-2,3)+2*(x1-2*x2),
                                    -4*(x1-2*x2)])

get_alpha = lambda ynext, ynow: (np.linalg.norm(ynext)**2) / (np.linalg.norm(ynow)**2)

def printer(index):
    print("X:",xList[index], "D:",dList[index], "Z:",zList[index], "l:",lList[index], "a:",aList[index])
    
# Initialization Step
xList=[]
dList=[]
zList=[]
aList=[]
lList=[]
eps=0.01

x1=0
x2=3
d1=fgradient(x1,x2)[0]
d2=fgradient(x1,x2)[1]
z=f(x1,x2)

xList.append((x1,x2))
dList.append((d1,d2))
zList.append(z)
aList.append("nil")
lList.append("nil")

while np.linalg.norm(fgradient(x1,x2)) >= eps:

    printer(-1)

    lambd= golden_search(xList[-1], dList[-1],verbose=False)
    lList.append(lambd)
    
    #print   ('z =' , z,'x=(',x1,',',x2,') d=(',d1,',', d2,')', 'lambda=', lambd, 'alpha=', alpha)
    x1=xList[-1][0]-lambd*dList[-1][0]
    x2=xList[-1][1]-lambd*dList[-1][1]
    xList.append((x1,x2))
    z=f(x1,x2)
    zList.append(f(x1,x2))
    
    alpha = get_alpha(fgradient(xList[-1][0],xList[-1][1]),
                     fgradient(xList[-2][0],xList[-2][1]))
    aList.append(alpha)
    
    d1=fgradient(xList[-1][0],xList[-1][1])[0] + alpha*dList[-1][0]
    d2=fgradient(xList[-1][0],xList[-1][1])[1] + alpha*dList[-1][1]
    dList.append((d1,d2))

print("*** Final Solution ***")
printer(-1)

