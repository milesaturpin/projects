import numpy as np
from numpy.linalg import * 
import matplotlib.pyplot as plt
from random import *
import math

n=100
x = [i for i in range(1,n+1)]
y = [i*i+randint(-2500,2500) for i in range(1,n+1)]
#y = [(0.001*i**2)+randint(-1,1) for i in range(1,n+1)]
z = [i+randint(-3,3) for i in x]
plt.scatter(x, y)

def reg(x,y,A):

	b = np.matrix([y]).transpose()
	normal = inv(A.transpose()*A)*A.transpose()*b

	#print("\nData points:")
	#for i in range(0,len(x)):
	#	print("(%d,%d)" % (x[i],y[i]), sep=' ',end='',flush=True)

	return normal

def linReg(x, y):
	ones = [1] * len(x)
	A = np.matrix([x,ones]).transpose()

	normal = reg(x,y,A)
	m = normal[0,0]
	b = normal[1,0]
	fit = [m*i+b for i in x]

	print("\n \nBest fit:")
	print("y = %.2fx + %.2f \n" % (m,b))	

	plt.plot(x,fit)

def quadReg(x,y):
	ones = [1] * len(x)
	A = np.matrix([np.multiply(x,x),x,ones]).transpose()

	normal = reg(x,y,A)
	a = normal[0,0]
	b = normal[1,0]
	c = normal[2,0]
	fit = [a*i*i + b*i + c for i in x]

	print("\n \nBest fit:")
	print("y = %.2fx^2 + %.2fx + %.2f \n" % (a,b,c))

	plt.plot(x,fit)

quadReg(x,y)
linReg(x,y)
plt.show()