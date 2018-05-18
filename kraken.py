import sys
import os

# Complete the function below.

"""
def krakenCount(m, n):
	if m == 1 or n == 1: return 1
	return krakenCount(m-1,n) + krakenCount(m-1,n-1) + krakenCount(m,n-1)
"""

# This is a memoized version of the above recursive function
def  krakenCount(m, n):
    # initialize a grid to store intermediate values, with base case val=1 when m or n is 0
    grid = [[1]*n]
    i = 0
    while i < m-1:
        grid.append([1] + [0]*(n-1))
        i += 1

    for i in range(1,m):
        for j in range(1,n):
            # number of paths through a given square is the sum of the
            # number of paths going through the squares to the right, diagonal, and down
            grid[i][j] = grid[i][j-1] + grid[i-1][j] + grid[i-1][j-1]
    
    return grid[m-1][n-1]
    
_m = int(input());

_n = int(input());

res = krakenCount(_m, _n)
print(res)