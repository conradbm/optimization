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

# randomly initialize the weights
w = np.random.randn(D + 1)


def sigmoid(z):
	return np.exp(z)/(1+np.exp(z))


def likelihood(w):
	total=0
	for i in range(Xb.shape[0]):
		pos_res = T[i]*np.log(sigmoid(Xb[i,:].dot(w)))
		neg_res = (1-T[i])*(1-np.log(sigmoid(Xb[i,:].dot(w))))
		total += pos_res
		total += neg_res
	return total

def grad_likelihood(w):
	wj = np.zeros(Xb.shape[1])
	for j in range(Xb.shape[1]):
		for i in range(Xb.shape[0]):
			left = T[i]*Xb[i,j]
			right = Xb[i,j]*sigmoid(Xb[i,:].dot(w))

		wj[j] = left - right
	return wj


# GRADIENT ASCENT
print("GRADIENT ASCENT")
print_buf=1000
etol = 1e-5
learning_rate=1.0
_=0
while True:

	if grad_likelihood(w).sum() <= etol:
		break

	w += learning_rate*grad_likelihood(w)

	if _ % print_buf == 0:

		print("Likelihood {}".format(likelihood(w)))
		print("Gradient {}".format(grad_likelihood(w)))
		print("Delta {}".format(grad_likelihood(w).sum()))
	
	_+=1
print("Final likelihood {}".format(likelihood(w)))
print("Final params {}".format(w))
print("Final preds {}".format(sigmoid(Xb.dot(w))>0.5))
print("Targets {}".format(T))

print("Accuracy {}".format())
