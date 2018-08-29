def longestRun(L):
	maxCount = 1
	subCount = 1
	for i in range(len(L)-1):
		if L[i] <= L[i+1]:
			subCount += 1
		else:
			if subCount > maxCount:
				maxCount = subCount
				subCount = 1
	if subCount > maxCount:
		return subCount
	else: 
		return maxCount

print(longestRun([1, 2, 3]) == 3)
print(longestRun([1, 2, 3, 0, 1, 2, 3, 4]) == 5)
print(longestRun([9, 8, 7, 1, 2, 3, 4]) == 4)
print(longestRun([1]) == 1)