import random

def stupid_sort(L): 
	count = 0
	while L != sorted(L):
		random.shuffle(L)
		print(L)
		count += 1 
	print("Attempts: " + str(count))

L = [9,7,5,3,1,0] 

stupid_sort(L)