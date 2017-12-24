import compiler
import re

raw_file = """max 10*x1 + 12*x2-x3        -x4
s.t.
0.1*x1 +0.2*x2>=100
x2<=200
x3+x4 >= 100
"""

objectiveRE = r'[max|min]'
isObjective = (lambda s: not (re.match(objectiveRE, s)==None))
isMax = (lambda x: x == "max")
isMin = (lambda x: x == "min")
isSt = (lambda x: x == "s.t.")

lines=raw_file.split("\n")

if isMax(lines[0][:3]):
    lines[0] =lines[0].split("max")[1]
else:
    lines[0] =lines[0].split("min")[1]

lines = [l.replace(" ","") for l in lines]            

trees = []
for line in lines:

    if isSt(line): continue # constraints begin
    trees.append(compiler.parse(line))

print(trees[0].getChildren())

def get_leaf(tree):
    # no children
    if len(tree.getChildren()) == 0:
        print tree
    else:
        # left child exists
        # right child exists
