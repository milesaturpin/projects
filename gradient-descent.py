import random 
import matplotlib.pyplot as plt
import math
import numpy as np

ALPHA = 0.1
RUNS = 100

x = [i/10 for i in range(0, 100)]
y = [i/10 + random.uniform(0,10*math.cos(i)) for i in range(0, 100)]

# x = [i/10 for i in range(0, 2)]
# y = [i/10 for i in range(0, 2)]

### GRADIENT DESCENT

X = np.vstack((x,np.ones(len(x))))
Y = np.array([y])
P = np.array([3,0])
Yhat = np.dot(np.transpose(X),P)

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
	print(val)
	return(0.5 * val / np.size(y))


def delta(theta, x, y, elt):
	yhat = np.dot(theta, x)
	val = np.sum(yhat - y) * elt
	return(ALPHA * val / np.size(y))

def update(theta,x,y):
	vfunc = np.vectorize(lambda elt: delta(theta, x, y, elt))
	diff = vfunc(theta)
	return theta - diff

cost_lst = []

P = update(P,X,Y)
cost_lst.append(cost(P,X,Y))
P = update(P,X,Y)
cost_lst.append(cost(P,X,Y))

while cost_lst[-1] - cost_lst[-2] > 1ˇˇ:
	P = update(P,X,Y)
	cost_lst.append(cost(P,X,Y))


Yhat = np.dot(np.transpose(X),P)
plt.scatter(x,y)
plt.plot(x,Yhat)
plt.show()

plt.plot([x for x in range(len(cost_lst))],cost_lst)
plt.show()

print(5/3)




# ### ANALYTIC SOLUTION

# A = np.array([x,y])