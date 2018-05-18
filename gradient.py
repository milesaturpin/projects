import csv
import numpy
import math
import matplotlib.pyplot as plt 
import time
from inspect import signature

# f = open('~/Desktop/data.csv','r')
# reader = csv.reader(f)

# data = []

# row_num = 0
# for row in reader:
# 	if row_num == 0:
# 		data = [[]] * len(row)
# 	# 	header = row
# 	else:
# 		col_num = 0 
# 		for col in row:
# 			data[col_num].append[col]
# 			col_num += 1

# 	row_num += 1

# print(data)

# f.close()



h = 0.001

def rangef(start, end, step):
	return [i*step for i in range(start*int(1/step),end*int(1/step))]

"""
def derivAt(fn,x):
		return round((fn(x+h)-fn(x))/h,3)
"""
def deriv(fn):
	return lambda x: (fn(x+h)-fn(x))/h



#dydx_cos = deriv(math.cos())

start = time.time()
class Function:

	def __init__(self,fn):
		self.fn = fn
		self.sig = signature(fn)
		self.params = self.sig.parameters

	def derivn(self,n):
		current = self.fn
		while n > 0:
			current = deriv(self.fn)
			n = n - 1
		return current

	def derivx(self):
		return lambda x,y: (fn(x+h,y)-fn(x,y))/h

	def derivy(self):
		return lambda x,y: (fn(x,y+h)-fn(x,y))/h


	# def partial(fn, var):
	# 	par = self.params
	# 	i = 0
	# 	for i in range(len(par)):
	# 		if par[i] == var:
	# 			par[i] = var + h 
	# 	# get position of var in params list
	# 	# return params list w/ that var modified to be var+h
	# 	# call function with params
 # 		return lambda 

	# def derivList(self,n):
	# 	lst = [self.fn]
	# 	while len(lst) < n+2:
	# 		lst.append(deriv(lst[-1]))
	# 	return lst

	def __str__(self):
		return str(self.sig)

Cube = Function(lambda x: x*x*x - 6*x*x + 2*x - 6)

print(str(Cube))

Plane = Function(lambda x,y,z: x+y+z)
print(str(Plane))






