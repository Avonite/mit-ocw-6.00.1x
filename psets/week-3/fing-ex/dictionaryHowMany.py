animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    """
    aDict: a dictionary
    counts the number of keys in the dictionary
    """
    number = 0
    for i in aDict.values():
        number += len(i)
    return number

print(how_many(animals))
