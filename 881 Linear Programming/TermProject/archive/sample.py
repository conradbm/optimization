#
# Blake Conrad 
# IMSE 881 Linear Programming Final Project
#
# Excel Sheet Reproduction (BASELINE)
#
# This script is meant to reproduce the algorithm in spreadsheet 
# Ex. 7.2 Primal Scaling Algorithm is working for standard LPs.
#


import numpy as np


A = np.matrix([[0,0,1,-1],
			   [1,1,1,1]])
b = np.array([0,1])
c = np.array([-1,0,0,0])

x0 = np.array([0.01, 0.01, 0.49, 0.49])
w0 = np.array([0, 0])
s0 = np.array([0,0,0,0])
gap = 1000000

print("Gap {}".format(gap))

it = 0 
verbose = False

while gap > 0.0001:
	
	print(it)

	X0 = np.diag(x0)
	

	AX_SQUARED = A.dot(X0**2)

	INV_AX_SAURED_A_TRANSPOSE = np.linalg.inv(AX_SQUARED.dot(A.T))


	w1 = INV_AX_SAURED_A_TRANSPOSE.dot(AX_SQUARED).dot(c.T)


	s1 = c - A.T.dot(w1.T).T


	alpha = 0.99

	dy = -1*np.multiply(x0, s1)


	tmp = -1*alpha/dy
	min_alpha_over_dy = np.min(tmp[tmp > 0])


	dx = X0.dot(dy.T)


	Adx = A.dot(dx)


	dy_dist = np.abs(np.sum(dy))


	x0 = x0 + (min_alpha_over_dy*dx).T
	x0 =np.asarray(x0)[0]

	w0 = w1
	s0 = s1

	gap = dy_dist

	it += 1

	if verbose:
		print("X0 {}".format(X0))
		print("AX_SQUARED {}".format(AX_SQUARED))
		print("INV_AX_SAURED_A_TRANSPOSE {}".format(INV_AX_SAURED_A_TRANSPOSE))
		print("w_k+1 {}".format(w1))
		print("s_k+1 {}".format(s1))
		print("dy_k+1 {}".format(dy))
		print("min_alpha_over_dy {}".format(min_alpha_over_dy))
		print("dx {}".format(dx))
		print("Adx {}".format(Adx))
		print("dy_k+1_dist {}".format(dy_dist))
		print("x_k+1 {}".format(x0))
