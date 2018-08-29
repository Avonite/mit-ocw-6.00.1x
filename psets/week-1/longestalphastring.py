s = 'abc'
subStr = ''
start = 0
end = 0

for i in range(len(s)):
    if i == len(s) - 1:
        if len(subStr) < len(s[start:end]):
            subStr = s[start:end]
        break
    if s[i] > s[i+1]:
        end = i + 1
        if len(subStr) < len(s[start:end]):
            subStr = s[start:end]
        start = end

print("Longest substring in alphabetical order is: " + subStr)
