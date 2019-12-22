#!/usr/bin/env python
# coding: utf-8

# # Blake Conrad
# 
# ## Final Project | Implement Interior Point Algorithm
# 
# ### Algorithm Implemented: Primal Affine Scaling Algorithm (Lecture 10)

# Import Numerical Computing Environment Packages

# In[162]:


import numpy as np
import matplotlib.pyplot as plt
import time


# # Problem 1:
# 
# Reproduce example in Lecture 10 notes using Primal Affine Scaling Algorithm

# In[163]:


A = np.matrix([[1, -1, 1, 0],
               [0, 1 , 0, 1]])
b = np.array([15, 15])
c = np.array([-2, 1, 0, 0])
N = A.shape[0]
M = A.shape[1]
print("A.shape{}".format(A))
print("b.shape {}".format(b))
print("c.shape {}".format(c))
print("{} constraints".format(N))
print("{} dimensions".format(M))


# In[166]:


def primal_interior_feasible(x):
    return (x > 0).all()

def make_feasible(z):
    z[z < 0 ] = max(0.1, z.max())
    return z

def dual_interior_feasible(s):
    return (s > 0).all()

def get_IBFS(dim):
    x0 = np.random.randn(dim)
    it=0
    while not primal_interior_feasible(x0):
        x0 = np.random.randn(dim)
        it+=1
    print("Took {} iterations to find IBFS.".format(it))
    return x0

def get_dual(X):
    w = np.linalg.inv(A.dot(X**2).dot(A.T)).dot(A).dot(X**2).dot(c)
    s = c - A.T.dot(w.T).T
    return w, s

def get_duality_gap(x,s):
    return x.dot(s.T)

def interior_point(A0,b0,c0,M0,etol=0.0001,alpha=0.1):
    
    # Get IBFS
    x0 = get_IBFS(M0)
    
    # Diagonalize
    X0 = np.diag(x0)
    
    # Get dual variables and dual slack
    w0, s0 = get_dual(X0)
    
    # Make dual feasible
    if not dual_interior_feasible(s0):
        s0 = make_feasible(s0)
    
    # Get initial duality gap
    gap = get_duality_gap(x0, s0).tolist()[0][0]
    it = 0
    gaps=[]
    iters=[]
    zs=[]
    while gap > etol:

        # Get primal scaling direction of improvement
        dy = -X0.dot(s0.T)

        # Get next best point
        x0 = x0 + alpha*X0.dot(dy).T

        # Make primal feasible
        if not primal_interior_feasible(x0):
            x0 = make_feasible(x0)

        # Get dual slack
        X0 = np.diag(np.asarray(x0)[0])
        w0, s0 = get_dual(X0)

        # Make dual feasible
        if not dual_interior_feasible(s0):
            s0 = make_feasible(s0)

        # Get duality gap
        gap = get_duality_gap(x0, s0).tolist()[0][0]
        it += 1
        z = x0.dot(c)
        
        # Record data
        gaps.append(gap)
        iters.append(it)
        zs.append(z)
        
        print("Iteration {}, Duality Gap {}".format(it, gap))


    print("Final Duality Gap {}".format(gap))
    print("Primal Variables {}".format(x0))
    print("Dual Slack Variables {}".format(s0))
    print("Dual Variables {}".format(w0))
    return x0,w0,s0,gaps,iters,zs


# In[170]:


x0,w0,s0,gaps,iters, zs=interior_point(A,b,c,M,etol=0.001)


# In[171]:


plt.scatter(iters,gaps)
plt.title("Lecture 10 Problem | Duality Gap")
plt.xlabel("Iteration")
plt.ylabel("Gap")
plt.show()


# In[172]:


plt.scatter(iters,zs)
plt.title("Lecture 10 Problem | Objective Function")
plt.xlabel("Iteration")
plt.ylabel("z")
plt.show()


# In[ ]:





# # Problem 2
# 
# Reproduce the blending problem

# In[103]:


import scipy.io


# In[174]:


D = scipy.io.loadmat('BLEND.mat')


print("Saving data")
A = D["A"].todense()
b = D["b"].reshape(-1)
c = D["c"].reshape(-1)
lb = D["lbounds"]
ub = D["ubounds"]
N = A.shape[0]
M = A.shape[1]
print("Confirming data shapes")
print("A {}".format(A.shape))
print("b {}".format(b.shape))
print("c {}".format(c.shape))
print("lb {}".format(lb.shape))
print("ub {}".format(ub.shape))


# In[175]:


def primal_interior_feasible(x):
    return (x > 0).all()

def make_feasible(z):
    z[z < 0 ] = max(0.1, z.max())
    return z

def dual_interior_feasible(s):
    return (s > 0).all()

def get_IBFS(dim):
    x0 = np.random.randn(dim)
    x0 = make_feasible(x0)
    return x0

def get_dual(X):
    w = np.linalg.inv(A.dot(X**2).dot(A.T)).dot(A).dot(X**2).dot(c)
    s = c - A.T.dot(w.T).T
    return w, s

def get_duality_gap(x,s):
    return x.dot(s.T)

def interior_point(A0,b0,c0,M0,etol=0.0001,alpha=0.1):
    
    A = A0
    b = b0
    c = c0
    M = M0
    
    # Get IBFS
    x0 = get_IBFS(M)
    
    # Diagonalize
    X0 = np.diag(x0)
    
    # Get dual variables and dual slack
    w0, s0 = get_dual(X0)
    
    # Make dual feasible
    if not dual_interior_feasible(s0):
        s0 = make_feasible(s0)
    
    # Get initial duality gap
    gap = get_duality_gap(x0, s0).tolist()[0][0]
    it = 0
    gaps=[]
    iters=[]
    zs=[]
    while gap > etol:

        # Get primal scaling direction of improvement
        dy = -X0.dot(s0.T)

        # Get next best point
        x0 = x0 + alpha*X0.dot(dy).T

        # Make primal feasible
        if not primal_interior_feasible(x0):
            x0 = make_feasible(x0)

        # Get dual slack
        X0 = np.diag(np.asarray(x0)[0])
        w0, s0 = get_dual(X0)

        # Make dual feasible
        if not dual_interior_feasible(s0):
            s0 = make_feasible(s0)

        # Get duality gap
        gap = get_duality_gap(x0, s0).tolist()[0][0]
        it += 1
        z=x.dot(c)
        
        # Record data
        gaps.append(gap)
        iters.append(it)
        zs.append(z)
        print("Iteration {}, Duality Gap {}".format(it, gap))


    print("Final Duality Gap {}".format(gap))
    print("Primal Variables {}".format(x0))
    print("Dual Slack Variables {}".format(s0))
    print("Dual Variables {}".format(w0))
    return x0,w0,s0,gaps,iters,zs

x0,w0,s0,gaps,iters,zs=interior_point(A,b,c,M,etol=0.01)


# In[179]:


plt.scatter(iters,gaps)
plt.title("Blending Problem | Duality Gap")
plt.xlabel("Iteration")
plt.ylabel("Gap")
plt.show()


# In[178]:


print("Final Solution {}".format(x0.dot(c)))


# In[ ]:




