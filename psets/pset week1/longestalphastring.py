s = 'azc'
longStr = ""
nxt = 1

for i in s:
    if i <= s[nxt]:
        longStr += i
        nxt += 1
    else:
        longStr += i

print(longStr)       