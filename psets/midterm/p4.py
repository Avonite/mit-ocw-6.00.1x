def dotProduct(listA, listB):
	'''
	listA: a list of numbers
	listB: a list of numbers of the same length of listA
	'''
	total = 0
	for i in range(len(listA)):
		total += listA[i]*listB[i]
	return total

listA = [-1, -2]
listB = [3, 4]

print(str(dotProduct(listA, listB)))
