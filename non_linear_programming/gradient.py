import simpy


x0=(0,0)
f= simpy.Eq(3*x**2+x*y+y**2+x+2)
str_vars = [str(a) for a in f.atoms() if not str(a).isdigit()]
vars  = [a for a in f.atoms() if not str(a).isdigit()]

f=3*x**2+x*y+y**2+x+2
fgradient=[sympy.diff(f,var) for var in vars]
xk=x0

direction=[i.evalf(subs={'x':xk[0],’y’:xk[1]}) for i in fgradient]
direction_lambda = [Symbol('lambda')*val for val in direction]

xk = [direction[i]-direction_lambda[i] for i in range(len(direction))]
flambda  = f.subs({x:xk[0], y:xk[1]})

dflambda = flambda.diff()

eq1 = str(dflambda)
eq1 = eq1.replace("lambda", "l")
l=10

eval(eq1) #evaluated the derivative of the original function substituted for lambda @ a value of lambda.
