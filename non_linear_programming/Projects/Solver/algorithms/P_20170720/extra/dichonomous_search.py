
# coding: utf-8

# In[4]:


from __future__ import division

f = lambda x: x**2 - (1/10)*x
f = lambda x: x**2 - 10*x

#Bazaraa, M., S., Sherali H., D, Shetty, C., M.
#Nonlinear Programming Theory and Algorithms Third Edition. 
#Wiley-Interscience 2006.\n",
def dichotomous_search(low=0,high=1,eps=0.1, verbose=False):

    if verbose:
        print("******************************")
        print("Executing Dichotomous Search")
        print("*******************************")

    lam=list()
    mu=list()
    a=list()
    b=list()
    a.append(low)
    b.append(high)
    k=0
    if verbose:
        print("************************")
        print(("[a,b]"), "|b[k]-a[k]|")
        print("************************")
    while True:
        if abs(b[k]-a[k])<=eps:
            break
        if verbose:
            print((a[k], b[k]), abs(b[k]-a[k]))
            print((b[k], a[k]), abs(b[k]-a[k]))
        lam.append(((a[k]+b[k])/2) - eps)
        mu.append(((a[k]+b[k])/2) + eps)
        if(f(lam[k]) < f(mu[k])):
            a.append(a[k])
            b.append(mu[k])
        else:
            a.append(lam[k])
            b.append(b[k])
        k+=1
        # If we are the exact same don't waste our time, exit
        if(abs(b[k]-a[k]) == abs(b[k-1]-a[k-1])):
            break

    return (a[-1],b[-1])
dichotomous_search(low=0,high=1,eps=0.1, verbose=True)

