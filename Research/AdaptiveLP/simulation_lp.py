import numpy as np
from scipy.optimize import minimize

def simulate_move_data(N=10,T=5):
    return np.abs(np.random.randn(N,T)), np.random.randn(N,T)

def get_optimal_moves(data, x0, N, T):
    
    def f(x):
        return -np.sum([data[i,j]*x.reshape(N,T)[i,j] for i in range(x.reshape(N,T).shape[0]) for j in range(x.reshape(N,T).shape[1])])
    
    eq_cons = {'type': 'eq',
               'fun' : lambda x: np.array([np.sum(w)-1 for w in x.reshape(N,T).T])}       # sum_i(Wij)=1 for all j // normalize weight columns
    ineq_cons = {'type': 'ineq',
                 'fun' : lambda x: np.array([w for w in x])} # Wij >= 0 for all i,j // only positive weights
    
    res = minimize(f, x0,
                   constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9})
    return res.x.reshape(N,T)

NUM_BATCHES=1000
N=10
T=5
X = np.empty((NUM_BATCHES, N, T))
for i in range(NUM_BATCHES):
    print(i)
    data,x0 = simulate_move_data(N=N, T=T)
    x = get_optimal_moves(data,x0, N, T)
    X[i,:,:]=x

np.set_printoptions(suppress=True)
print("Results {}".format(X.shape))
print(np.average(X, axis=0))