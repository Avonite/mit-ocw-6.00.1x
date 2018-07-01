def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: list of unique keys in aDict
    '''
    uniqueKeys = []
    # Transform aDict keys to list of keys
    keys = list(aDict.keys())
    # Make copy of keys
    keysCopy = keys[:]
    # Iterate over keys and modify keysCopy
    for k in keysCopy:
    	if keysCopy.count(k) == 1:
    		uniqueKeys.append(k)
    return uniqueKeys

    
d = {1: 1, 2: 2, 3: 3, 7: 2}

print(uniqueValues(d))


# Write a Python function that returns a list of keys in aDict that map to integer values that are unique
# (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order.
# (If aDict does not contain any unique values, you should return an empty list.)

# This function takes in a dictionary and returns a list.

