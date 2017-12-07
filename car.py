import matplotlib.pyplot as plt 
import math

def derivAt(fn,x):
	h = 0.000001
	return round((fn(x+h)-fn(x))/h,3)

def deriv(fn):
	return lambda x: derivAt(fn,x)

def rangef(start,end, step):
	return [i*step for i in range(start,end*int(1/step))]

sq = lambda x: x*x
sq_dydx = deriv(sq)
cos = lambda x: math.cos(x)
cos_dydx = deriv(cos)

step = 0.01
x = rangef(0,20,step)
y_lst = lambda fn: [fn(x) for x in x]
y = y_lst(cos)
y_dydx = y_lst(cos_dydx)

plt.plot(x,y)
plt.plot(x,y_dydx)
plt.show()
