from cs50 import get_int
from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#0 Use alternative way of reading inputs - using library (0.5p)
x = get_int("x: ")
y = get_int("y: ")

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
print('task1')

print(f"x*pi: {x*pi}")
print(f"y*pi: {y*pi}")
print(f"x*pi**2:  {x*pi**2}")
print(f"y*pi**2:  {y*pi**2}")

#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
print('task2')
xyIsEven = x and y % 2 == 0
xyDivisible = x % y == 0
b = x / y
xyIsEvenDivisible = b if xyIsEven and xyDivisible else 'X,Y are not even and not divisible'
print(xyIsEvenDivisible)

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
print('task3')
xDy = x % y == 0
xDyResult ='x is divisible by y' if xDy else 'x is not divisible by y'
print(xDyResult)

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
print('task4')
a = x / y
print("{0:.2f}".format(round(a,2)))

#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
print('task5')

x_knots = np.linspace(-5,5,201)
y_knots = np.linspace(-5,5,201)
X, Y = np.meshgrid(x_knots, y_knots)
Z = X**2 + Y**3 + 4*X*Y**2
ax = Axes3D(plt.figure(figsize=(10,7)))
ax.plot_surface(X, Y, Z, cmap=plt.cm.rainbow)
plt.show()

x_knots = np.linspace(-500,5*np.pi,1001)
y_knots = np.linspace(-500,5*np.pi,1001)
P = np.linspace(0,2*np.pi, 1001)
X, Y = np.meshgrid(x_knots, y_knots)
Z = X**2 + Y**3 + 4*X*Y**2 + np.cos(P)
ax = Axes3D(plt.figure(figsize=(10,7)))
ax.plot_surface(X, Y, Z, P, cmap=plt.cm.rainbow)
plt.show()

#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)