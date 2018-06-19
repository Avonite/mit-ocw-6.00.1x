animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    number = 0
    nameOfKey = ""
    for i in aDict:
        if len(aDict[i]) > number:
            number = len(aDict[i])
            nameOfKey = i           
    return nameOfKey

print(biggest(animals))
            
    