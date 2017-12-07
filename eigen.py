import numpy as np
from numpy.linalg import * 
import matplotlib.pyplot as plt
from random import *
import math

A = np.array([
	[ 1, 4,-3, 4, 5], 
	[ 0,-2, 8, 7,-3],
	[-2,-2, 9, 8,-2],
	[ 2,-10,3, 3,14],
	[-4, 2, 7,-9, 0]
	]).astype(float)
B = np.array([
	[1,2],
	[3,4]
	])
x = np.array([
	[ 1],
	[-2],
	[ 3],
	[-4],
	[-5]
	]).astype(float)

def gauss_reduce(A, j=0):

	# jth column
	col = A[:,j]
	# pivot at row j
	pivot = col[j]

	# check to see if last column
	if j+1 == len(col):
		return A
	else:
		# iterate through col and reduce rows under pivot 
		for i in range(j+1,len(col)):
		
			entry = col[i]
			if entry == 0:
				continue
			else:
				factor = entry / pivot
				A[i] = A[i] - factor * A[j]
		return gauss_reduce(A, j+1)

def diag(A):
	if A.size == 1:
		return A[0,0]
	else:
		return A[0,0] * diag(A[1:,1:])

def det(A):
	return diag(gauss_reduce(A))

print(det(A))
#print(np.round(gauss_reduce(A),3))






#eigenvalues = np.linalg.eigvals(A)
#print(eigenvalues)