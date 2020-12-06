import math
import csv
from library_week7 import *

e = 2.718281828459

def f(x,y):
    z=(y*(math.log(y,e)))/x
    return z

print("The equation is y'=y.ln(y)/x")
print()

h= [0.5, 0.1, 0.05, 0.02]
for i in range(len(h)):
    x, y = euler(f, 2, e, h[i])
    name= "Q1a with h="+str(h[i])
    create_csv(name, x, y)
    print("The equation is solved by euler's method with h=", h[i])
    print("The result is appended in csv file, Q1a with h=", h[i])
    print()

'''
The equation is y'=y.ln(y)/x

The equation is solved by euler's method with h= 0.5
The result is appended in csv file, Q1a with h= 0.5

The equation is solved by euler's method with h= 0.1
The result is appended in csv file, Q1a with h= 0.1

The equation is solved by euler's method with h= 0.05
The result is appended in csv file, Q1a with h= 0.05

The equation is solved by euler's method with h= 0.02
The result is appended in csv file, Q1a with h= 0.02
'''