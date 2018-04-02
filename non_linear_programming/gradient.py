import sympy
import numpy as np

## Consider a two-dimensional problem.

# Initialization:
x0 = np.random.randint(1,100, size=2)
epsilon = 0.001
k=0
x, y, lamda = sympy.symbols('x y lamda')
f = 3*x**2+x*y+y**2+x+2
fgradient = [f.diff(var) for var in (x, y)]   # calling diff as a method is convenient
xk=[]
xk.append(x0)
k+=1
print(xk)

# Procedure:
for i in range(1000):
    
    direction = [i.subs({x: xk[k-1][0], y: xk[k-1][1]}) for i in fgradient]
    xi = [xk[k-1][i] - lamda*direction[i] for i in range(len(direction))]
    flamda  = f.subs({x:xi[0], y:xi[1]})
    dflamda = flamda.diff()
    soln = sympy.solve(dflamda)[0] #Assuming lambda has only 1 root, so it is the best 
    xi = [i.subs({lamda:soln}).evalf() for i in xi]
    xk.append(np.array(xi))

    print("k-1: ",xk[k-1])
    print("k: ",xk[k])
    print("difference: ",abs(xk[k] - xk[k-1]))
    print ("Which elements are less than epsilon? ",abs(xk[k] - xk[k-1]) < epsilon)
    print("Are all less than epsilon? ", all(abs(xk[k] - xk[k-1]) < epsilon))
    if all(abs(xk[k] - xk[k-1]) < epsilon):
        break
    k= k + 1
local_optimum = xk[-1] #and if convex, it is global
local_optimum
# >> Soln: array([-0.181810432795123, 0.0908748033628853], dtype=object)


"""
import sympy
import numpy as np

## Consider a two-dimensional problem. minimize

x0 = np.random.randint(1,100, size=2)
epsilon = 0.001
k=0
x, y, lamda = sympy.symbols('x y lamda')
# This problem worked: ' 3*x**2+x*y+y**2+x+2
f = (x**2)*(y**2)
fgradient = [f.diff(var) for var in (x, y)]   # calling diff as a method is convenient
xk=[]
xk.append(x0)
k+=1

print("*** Initial *** ")
print("Pos:",xk)
print("Function:",f)
print("Gradient:",fgradient)
print("*** *** *** ")



direction = [i.subs({x: xk[k-1][0], y: xk[k-1][1]}) for i in fgradient]
print("Direction:", direction)
xi = [xk[k-1][i] + lamda*direction[i] for i in range(len(direction))]

# If the direction is 0,0 then no lambda exists, so your new position is just the old position.

print("Next position:", xi)
flamda  = f.subs({x:xi[0], y:xi[1]})
print("Function of lambda:",flamda)
dflamda = flamda.diff()

print("Derivative of function of lambda:", dflamda)
soln = sympy.solve(dflamda)
print("Solutions:", soln)
print("Type of solutions:", type(soln))

print("Optimal lambda: ", soln[0])

xi = [i.subs({lamda:soln[0]}).evalf() for i in xi]
xk.append(np.array(xi))

print("k-1: ",xk[k-1])
print("k: ",xk[k])
print("difference: ",abs(xk[k] - xk[k-1]))
print ("Which elements are less than epsilon? ",abs(xk[k] - xk[k-1]) < epsilon)
print("Are all less than epsilon? ", all(abs(xk[k] - xk[k-1]) < epsilon))

k= k + 1
xk
"""
