#
#
# mle.py
#
# Maximum Likelihood Estimation Using Gradient Descent and Newtons Method.
#
#
# Gradient Descent Brush Up: xk+1 <- xk + lam*grad(xk)
# Newtons Method Brush Up: xk+1 <- xk + lam*hesh_inv(xk)*grad(xk)
#
#
# This script is meant to illustrate how the 
#   Maximum Likelihood Estimator can be applied
#   to approximate the parameters of a logistic
#   regression. Below is the formulation:
#
#  Max. sum(yi*log(p(xi.dot(w)))  + (1-yi)*(1 - p(xi.dot(w)))
#  where p(z) = exp(z)/(1+exp(z))
#
#



import numpy as np


def get_data():
    N = 100
    D = 2

    X = np.random.randn(N,D)

    # center the first 50 points at (-2,-2)
    X[:50,:] = X[:50,:] - 2*np.ones((50,D))

    # center the last 50 points at (2, 2)
    X[50:,:] = X[50:,:] + 2*np.ones((50,D))

    # labels: first 50 are 0, last 50 are 1
    T = np.array([0]*50 + [1]*50)

    # add a column of ones
    # ones = np.array([[1]*N]).T # old
    ones = np.ones((N, 1))
    Xb = np.concatenate((ones, X), axis=1)

    return Xb,T

def sigmoid(z):
	return np.exp(z)/(1+np.exp(z))

def likelihood(w, Xb, T):
    total=0
    for i in range(Xb.shape[0]):
        z = Xb[i,:].dot(w)
        pos_res = T[i]*np.log(sigmoid(z))
        neg_res = (1-T[i])*(1-np.log(sigmoid(z)))
        total += pos_res
        total += neg_res
    return total


def grad_w(w, Xb, T):
    wj = np.zeros(Xb.shape[1])
    for j in range(Xb.shape[1]):
        for i in range(Xb.shape[0]):
            
            z = Xb[i,:].dot(w)
            left = T[i]*Xb[i,j]           
            right = Xb[i,j]*sigmoid(z)
        wj[j] = left - right
    return wj

"""
def grad_P(w, P, Xb, T):
    pkl = np.zeros((Xb.shape[1], Xb.shape[1]))
    for k in range(Xb.shape[1]):
        for l in range(Xb.shape[1]):
            for i in range(Xb.shape[0]):
                left = T[i]*Xb[i,k]*Xb[i,l]
                z = sigmoid(Xb[i,:].dot(P).dot(Xb[i,:].T).sum() + Xb[i,:].dot(w))
                right = Xb[i,k]*Xb[i,l]*sigmoid(z)
            pkl[k,l] = left - right
    return pkl
"""
def logistic_fit(Xb,
                 T,
                 print_buf=1000, 
                 etol=0.0001, 
                 learning_rate=1.0):

    
    
    # GRADIENT ASCENT
    print("Maximum Likelihood")
    print("Gradient Ascent")
        
    # randomly initialize the weights
    w = np.random.randn(Xb.shape[1])
    
    _=0
    while True:

        if grad_w(w, Xb, T).sum() <= etol:
            break

        w += learning_rate*grad_w(w, Xb, T)

        if _ % print_buf == 0:

            print("Likelihood {}".format(likelihood(w, Xb, T)))
            print("Gradient {}".format(grad_w(w, Xb, T)))
            print("Delta {}".format(grad_w(w, Xb, T).sum()))

        _+=1

    print("Final likelihood {}".format(likelihood(w, Xb, T)))
    print("Final params {}".format(w, Xb, T))
    z = Xb.dot(w)
    preds = np.array(sigmoid(z)>0.5, dtype=np.int)

    print("Final preds {}".format(preds))
    print("Targets {}".format(T))
    print("Accuracy: {}".format((preds == T).sum()/len(preds)))

    return w



Xb, T = get_data()
w = logistic_fit(Xb, 
                 T, 
                 print_buf=1000,
                 etol=0.001,
                 learning_rate=1.0)
