import random 
import matplotlib.pyplot as plt
import math
import numpy as np

ALPHA = 0.0001
RUNS = 100

x = [i for i in range(0, 10)]
y = [i + random.uniform(-0.001*i**2,0.001*i**2) for i in range(0, 10)]

#x = [i for i in range(0, 10)]
#y = [2*i for i in range(0, 10)]

### GRADIENT DESCENT

X = np.vstack((np.ones(len(x)),x))
Y = np.array([y])
P = np.array([60,100])
print(X)
print(P)
Yhat = np.dot(P,X)
# print(Yhat)

plt.scatter(x,y)
plt.plot(x,Yhat)
plt.show()

def cost(theta, x, y):
	yhat = np.dot(theta,x)
	# print(yhat)
	# print(y)
	# print((yhat-y))
	# print((yhat-y)**2)
	val = np.sum((yhat - y) ** 2)
	#print(val)
	return(0.5 * val / np.size(y))


def delta(yhat,x, y, index):
	
	# print(x)
	# print("yhat:")
	# print(yhat)
	# print("y:")
	print(y)
	print("diff:")
	print(yhat-y)
	diff = yhat - y
	# print(diff[0])
	val = 0
	# print(x)
	for i in range(len(diff[0])):
		#print(diff[0,i]*x[index,i])
		val += diff[0,i]*x[index,i]

	print("val:")
	# print(val)
	print(ALPHA * val / np.size(y))
	return(ALPHA * val / np.size(y))

def update(theta,x,y):
	# print(theta)
	# vfunc = np.vectorize(lambda elt: delta(theta, x, y, elt))
	# diff = vfunc(theta)
	yhat = np.dot(theta, x)
	diff = []
	for i in range(len(theta)):
		# print(delta(yhat,x, y, i))
		diff.append(delta(yhat, x, y, i))
	# print("theta, diff")
	# print(theta)
	# print(diff)
	# print(theta - diff)
	return theta - diff

cost_lst = []

# P = update(P,X,Y)
# cost_lst.append(cost(P,X,Y))
# P = update(P,X,Y)
# cost_lst.append(cost(P,X,Y))

while len(cost_lst) < 3 or cost_lst[-1] - cost_lst[-2] < -0.001:
	P = update(P,X,Y)
	cost_lst.append(cost(P,X,Y))

# print(cost_lst)
print(cost_lst[-1] - cost_lst[-2])

Yhat = np.dot(P,X)
plt.scatter(x,y)
plt.plot(x,Yhat)
plt.show()

plt.plot([x for x in range(len(cost_lst))],cost_lst)
plt.show()





# ### ANALYTIC SOLUTION

# A = np.array([x,y])