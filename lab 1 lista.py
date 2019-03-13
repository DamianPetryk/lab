#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
print('task1')
def y(x):
    return 2**x + 2*x +2
for i in range(56,101):
    print(y(i))


#2 ask the user for a number and print its factorial (1p)
print('task2')
print('Insert a number to print a factorial:')

n = int(input())
def fact(n):
    return 1 if n == 1 or n == 0 else n * fact(n - 1)
print(fact(n))


#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
print('task3')
tab = [ -1, -10, 12, -41, -9, 6, 56, -45]
print(min(tab))
print(tab.index(min(tab)))


#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
print('task4')
from matplotlib.pyplot import *
from numpy import *

x = linspace(-100, 100, 100)
y = 2*x + x**2
plot(x,y)
show()