from random import *
from functools import reduce
import time
import matplotlib.pyplot as plt

start = time.time()

def removeDuplicates1(lst):
	seen = []
	for elt in lst:
		if elt not in seen:
			seen.append(elt) 
		else: continue
	return seen

def removeDuplicates(lst):
	return list(set(lst))

def constructList(length):
	quant = {n: 5 for n in range(1,20001)}
	lst = []
	lst_set = []
	while len(lst) < length:
		num = randint(1,20000)
		if quant[num] > 0:
			lst.append(num)
			if quant[num] == 5:
				lst_set.append(num)
			quant[num] = quant[num] - 1
	return lst, len(lst_set)

size = range(1,11)
percents = []
for i in size: 

	sample_size = 5
	unique = 0
	for j in range(sample_size):
		birthday, unique_size = constructList(i*10000)
		unique = unique + unique_size
	avg = unique / sample_size
	percent = round(avg / 20000,3)
	percents.append(percent)

	# unique = list(map(lambda birthdays: len(removeDuplicates(birthdays)),birthdays_lst))

	# avg = reduce((lambda x, y: x+y), unique)/len(birthdays_lst)
	print("Select {2} --> Number unique: {0}... Percent: {1}".format(avg, percent, i*10000))

plt.plot(size,percents)
end = time.time()
print(end - start)

plt.show()


