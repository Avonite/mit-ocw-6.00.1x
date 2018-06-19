s = input("Please enter a string: ")
numBob = 0
count = 0

while count < len(s):
    if s[count:count+3] == "bob":
        numBob += 1
    count += 1

print(numBob)       
    
    
