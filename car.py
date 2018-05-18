import matplotlib.pyplot as plt 
import math
import time

h = 0.00001

def rangef(start, end, step):
	return [i*step for i in range(start*int(1/step),end*int(1/step))]

"""
def derivAt(fn,x):
		return round((fn(x+h)-fn(x))/h,3)
"""
def deriv(fn):
	return lambda x: (fn(x+h)-fn(x))/h

def partial(fn, var):
	return lambda 

#dydx_cos = deriv(math.cos())

start = time.time()
class Function:

	def __init__(self,fn, ):
		self.fn = fn

	def derivn(self,n):
		current = self.fn
		while n > 0:
			current = deriv(self.fn)
			n = n - 1
		return current

	# def derivList(self,n):
	# 	lst = [self.fn]
	# 	while len(lst) < n+2:
	# 		lst.append(deriv(lst[-1]))
	# 	return lst

	def __str__(self)

Cube = Function(lambda x: x*x*x - 6*x*x + 2*x - 6)
#Cos = Function(lambda x: math.cos(x))
# cube = Cube.derivn(0)
# cube1 = Cube.derivn(1)
# cube2 = deriv(deriv(lambda x: x*x*x - 6*x*x + 2*x - 6))
# cube3 = deriv(deriv(deriv(lambda x: x*x*x - 6*x*x + 2*x - 6)))



# end = time.time()
# print(end-start)

# start = time.time()
cube = Cube.derivList(5)[0]
cube1 = Cube.derivList(5)[1]
cube2 = Cube.derivList(5)[2]
cube3 = Cube.derivList(5)[3]

# end = time.time()
# print(end-start)

"""
#Functions
sq = lambda x: x*x
sq1 = derivn(sq,1)

cos = lambda x: math.cos(x)
cos1 = derivn(cos,1)

cube = lambda x: x*x*x - 2*x*x + 4*x - 8
cube1 = derivn(cube,1)
cube2 = derivn(cube,2) 
"""
#Plot Functions
step = 0.01
x = rangef(-2,5,step)
y_lst = lambda fn: [fn(x) for x in x]
y = y_lst(cube)
y1 = y_lst(cube1)
y2 = y_lst(cube2)
y3 = y_lst(cube3)

plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()
