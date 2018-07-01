# Write a function to flatten a list. The list contains other lists, 
# strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flat(aList):
	returnList = []
	for i in aList:
		if type(i) == list:
			return returnList + flat(i)
		else:
			returnList.append(i)
	return returnList

testList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 

print(flat(testList))