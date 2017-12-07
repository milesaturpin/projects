import numpy as np
import matplotlib.pyplot as plt
from random import *
import math

n= 30
x = [i for i in range(1,n+1)]
y1 = [-2*i+randint(-10,10)+100 for i in range(1,n+1)]
y2 = [-2*i+randint(-10,10)+65 for i in range(1,n+1)]

plt.scatter(x,y1)
plt.scatter(x,y2)
plt.show()
