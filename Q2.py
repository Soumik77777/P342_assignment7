import csv
import math
from library_week7 import *

def f(y,x):
    z=y*2/x
    return z

def rk(x0,y0):
    h = 0.01
    x, y, x1 = [], [], []
    y.append(y0)
    x.append(x0)
    x1.append(math.pow(x0, 2) / 9)
    for i in range(1, 800):

        k1=h * f(y[i-1],x[i-1])
        k2=h * f(y[i-1] + k1/2, x[i-1] + h/2)
        k3=h * f(y[i-1] + k2/2, x[i-1] + h/2)
        k4=h * f(y[i-1] + k3, x[i-1] + h)
        z = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4)/6
        y.append(z)
        x.append(x0 + (i * h))
        x1.append(math.pow(x[i],2)/9)
    write_csv("data1.csv", y, x)
    write_csv("data1c.csv", x1, x)


rk(3,1)