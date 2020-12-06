import math
import csv
from library_week7 import *

def f(x,y):
    z=6-((2*y)/x)
    return z

print("The equation is y'=6-(2y/x)")
print()

h= [0.5, 0.1, 0.05, 0.02]
for i in range(len(h)):
    x, y = euler(f, 3, 1, h[i])
    name= "Q1b with h="+str(h[i])
    create_csv(name, x, y)
    print("The equation is solved by euler's method with h=", h[i])
    print("The result is appended in csv file, Q1b with h=", h[i])
    print()


'''
The equation is y'=6-(2y/x)

The equation is solved by euler's method with h= 0.5
The result is appended in csv file, Q1b with h= 0.5

The equation is solved by euler's method with h= 0.1
The result is appended in csv file, Q1b with h= 0.1

The equation is solved by euler's method with h= 0.05
The result is appended in csv file, Q1b with h= 0.05

The equation is solved by euler's method with h= 0.02
The result is appended in csv file, Q1b with h= 0.02

'''