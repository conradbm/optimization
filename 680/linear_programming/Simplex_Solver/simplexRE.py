import re
"""
2x1 + x2 - 15x3
x1 <= 10
x1-10x2 >= 5
4x1 + 3x2 + 2x3 <= 100
x3 <= 10
x3 > 2
"""
t1 = "2x1 + x2 - 15x3"
e1 = r'(\d*)([a-z]+\d*)\s*([\+-]*)'
re.findall(e1, t1)

t2 = """
x1 <= 10\n
x1-10x2 >= 5\n
4x1 + 3x2 + 2x3 <= 100\n
x3 <= 10\n
x3 > 2\n
"""

e2 = r'((\d*)([a-z]+\d*)\s*([\+-]*))*\s*([<=|>=]*)\s*(\d*)'
re.findall(e2,t2)