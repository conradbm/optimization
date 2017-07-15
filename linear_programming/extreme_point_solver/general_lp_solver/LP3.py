
"""
Author: Blake Conrad
File Format:
max
z=2x+2y
s.t
y=x+1 x=y-1
y=2x x=y/2
"""

flatten = (lambda l: [item for sublist in l for item in sublist])

def get_file_lines(fileName):
    equation_file=[]
    with open(fileName, "r") as f_in:
        equation_file=f_in.readlines()
    return [i.strip("\n") for i in equation_file]

parsedFile = get_file_lines("equations.txt")

print 
print "Optimization Goal: ", str(parsedFile[0])
print "Objective Function: ", str(parsedFile[1])
print "Constraint Equations: ", parsedFile[3:]
print 

goal = parsedFile[0]
obj = parsedFile[1].split("=")[1]
obj = (lambda x,y: eval(obj))

constraints = parsedFile[3:]
constraints = flatten([c.split(" ") for c in constraints])
constraints = [c.split("=") for c in constraints]
constraints = [c[1] for c in constraints]
yevals=[constraints[i] for i in range(len(constraints)) if i % 2 == 0] #evens
xevals=[constraints[i] for i in range(len(constraints)) if i % 2 != 0] #odds

#ys = [lambda x: (x, eval(constraints[i+1])) for i in range(len(constraints)) if constraints[i] == 'y']
#xs = [lambda y: (eval(constraints[i+1]), y) for i in range(len(constraints)) if constraints[i] == 'x']

