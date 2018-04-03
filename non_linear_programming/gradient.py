import sympy
import numpy as np

## Consider a two-dimensional problem.

# Initialization:
print("Initialization ... \n")
print
x0 = np.random.randint(1,100, size=2)
x0 = np.array([50,410])
epsilon = 0.001
k=0
x, y, lamda = sympy.symbols('x y lamda')
f = 3*x**2+x*y+y**2+x+2 #worked
f = (x**2)*(y**2) #worked
f = x**3+(1/x*y) #broke, so soln returned on sympy.solve(dflamda)
f = (x**3+1)*y
f = (x**2)*(y**2)

fgradient = [f.diff(var) for var in (x, y)]   # calling diff as a method is convenient
xk=[]
xk.append(x0)
k+=1

print ("Create hyperparameters ...  \n")
print ("Initial Position:", x0)
print ("Threshold:", epsilon)
print ("Symbols:", x,y,lamda)
print ("F(x,y):", f)
print ("Gradient(F(x,y)):", fgradient)
print ("\n")

print ("Execute Procedure ...  \n")
# Procedure:
for i in range(5):
    

    # create dictionary for each atom the value from xk-1 then feed


    direction = [i.subs({x: xk[k-1][0], y: xk[k-1][1]}) for i in fgradient]
    
    print("G(F(x_k-1[0], x_k-1[1]))=", direction)
    
    xi = [xk[k-1][i] - lamda*direction[i] for i in range(len(direction))]
    
    print("Next Position: xi (lamda): ", xi)
    
    # If the new point is = the last point, or the new direction is <0,0> we approached a tangent = 0, so we are done.
    # break
    if all([i==0 for i in direction]):
        break
    
    # create dictionary for each atom the value from xk-1 then feed

    flamda  = f.subs({x:xi[0], y:xi[1]})
    
    print ("F(lamda)= ", flamda)
    
    dflamda = flamda.diff()
    
    print("F'(lamda)= ",dflamda)
    
    soln = sympy.solve(dflamda) #Assuming lambda has only 1 root, so it is the best 
    
    if len(soln) == 0:
        print(soln)
        print("F'(lambda)=",dflamda)
        soln=dflamda
        #print("No solution to F'(lambda)=0.")
        #break
    else:
        soln=soln[0]
    
    #soln = soln[0]
    print("F'(lamda)= 0 --> lambda=",soln)
    
    xi = [i.subs({lamda:soln}).evalf() for i in xi]
    
    print("Next Position: xi (solved): ", xi)
    
    xk.append(np.array(xi))

    print ("*** Calculate changes in step *** ")
    print("Difference: |x[k-1] - x[k]| = ",abs(xk[k] - xk[k-1]))
    print ("Which elements are less than epsilon? ",abs(xk[k] - xk[k-1]) < epsilon)
    print("Are all less than epsilon? ", all(abs(xk[k] - xk[k-1]) < epsilon))
    
    if all(abs(xk[k] - xk[k-1]) < epsilon):
        print("Your change was sufficiently small, algorithm terminating.")
        break
    k= k + 1

print ("*** Procedure Complete *** \n")

local_optimum = xk[-1] #and if convex, it is global
print ("Local optimum at: ", local_optimum)



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
