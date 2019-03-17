import numpy as np
from scipy.optimize import minimize

def simulate_move_data(N=10,T=5):
    return np.abs(np.random.randn(N,T)), np.random.randn(N,T)

def get_optimal_moves(data, x0, N, T):
    
    def f(x):
        return -np.sum([data[i,j]*x.reshape(N,T)[i,j] for i in range(x.reshape(N,T).shape[0]) 
                                                        for j in range(x.reshape(N,T).shape[1])])
    
    eq_cons = {'type': 'eq',
               'fun' : lambda x: np.array([np.sum(w)-1 for w in x.reshape(N,T).T])}       # sum_i(Wij)=1 for all j // normalize weight columns
    ineq_cons = {'type': 'ineq',
                 'fun' : lambda x: np.array([w for w in x])} # Wij >= 0 for all i,j // only positive weights
    
    res = minimize(f, x0,
                   constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9})
    return res.x.reshape(N,T)

def get_optimization(data=None, batch_size=100,data_shape=(10,5)):
    

    # Simulate NUM_BATCHES datasets to get a single optimization output matrix.
    if data is None:
        N=data_shape[0]
        T=data_shape[1]
        X = np.empty((batch_size, N, T), dtype=np.float)
        for i in range(batch_size):
            print(i)
            data,x0 = simulate_move_data(N=N, T=T)
            x = get_optimal_moves(data,x0, N, T)
            X[i,:,:]=x
        
        Wij=np.average(X, axis=0) #averages accross first index (rows)
        Wij_move_sequence=np.argmax(Wij, axis=0) #argmax accross columns row-wise
        
        np.set_printoptions(suppress=True)
        print("Wij.shape {}".format(Wij.shape))
        print("Wij {}".format(Wij))
        print("Wij_move_sequence {}".format(Wij_move_sequence))
        return (Wij, Wij_move_sequence)
    else:
        N=data.shape[0]
        T=data.shape[1]
        x0=np.random.randn((N,T))
        x_opt = get_optimal_moves(data,x0, N, T)
        x_opt_sequence=np.argmax(x_opt, axis=0)
        np.set_printoptions(suppress=True)
        print("x_opt.shape {}".format(Wij.shape))
        print("x_opt {}".format(Wij))
        print("x_opt_sequence {}".format(x_opt_sequence))
        return (x_opt, x_opt_sequence)
#wijk,_=get_optimization(data=None, NUM_BATCHES=100,DATA_SHAPE=(10,5))
