def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Get longest string
    longest = s1
    shortest = s2
    lacedString = ''

    if len(s2) > len(s1):
    	longest = s2
    	shortest = s1

    for i in range(len(shortest)):
    	lacedString += s1[i] + s2[i]

    lacedString += longest[len(shortest):]

    return lacedString

print(laceStrings("abc", "def") == "adbecf")

print(laceStrings('', "def") == "def")

print(laceStrings('abcxyz', "def") == "adbecfxyz")

print(laceStrings('abc', "defxyz") == "adbecfxyz")

