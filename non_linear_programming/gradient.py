import simpy

# Remarks: xk should be a list, x0 should be initially appended, then xk should be appended at the end of each iteration

# Initialize:
x0=(0,0)
f= simpy.Eq(3*x**2+x*y+y**2+x+2)
str_vars = [str(a) for a in f.atoms() if not str(a).isdigit()]
vars  = [a for a in f.atoms() if not str(a).isdigit()]

f=3*x**2+x*y+y**2+x+2
fgradient=[sympy.diff(f,var) for var in vars]
x0
eps=0.001

# do {
    direction=[i.evalf(subs={'x':x0[0],’y’:x0[1]}) for i in fgradient]
    direction_lambda = [Symbol('lambda')*val for val in direction]

    xk = [direction[i]-direction_lambda[i] for i in range(len(direction))]
    flambda  = f.subs({x:xk[0], y:xk[1]})

    dflambda = flambda.diff()
    lam = solve(dflambda) #assuming only 1 lambda
    xk = [str(comp).replace("lambda",str(lam[0])) for comp in xk]
    k+=1
    #eq1 = str(dflambda)
    #eq1 = eq1.replace("lambda", "l")
    #l=10
    #eval(eq1) #evaluated the derivative of the original function substituted for lambda @ a value of lambda.
# } While ( | xk[k] - xk[k-1 | > eps  )


# better way
import sympy
x0 = (0,0)
x, y, lamda = sympy.symbols('x y lamda')
f = 3*x**2+x*y+y**2+x+2
fgradient = [f.diff(var) for var in (x, y)]   # calling diff as a method is convenient
# do{
xk = x0
direction = [i.subs({x: xk[0], y: xk[1]}) for i in fgradient]
xk = [xk[i] - lamda*direction[i] for i in range(len(direction))]
flamda = f.evalf(subs={x: xk[0], y: xk[1]})
dflambda = flambda.diff()
lam = solve(dflambda) #assuming only 1 lambda
xk = [i.subs({lamda:lam}) for i in xk]#untested
#flamda = sympy.lambdify(lamda, f.subs({x: xk[0], y: xk[1]}))
