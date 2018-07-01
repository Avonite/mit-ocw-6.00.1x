def myLog(x, b):
	'''
	x: positive integer
	b: positive integer; b>= 2

	returns: log_b(x), or the logarithm of x relative to a base b.
	'''
	count = -1
	product = 1
	while (product <= x):
		count += 1
		product *= b
	return count

print(str(myLog(16, 2)))