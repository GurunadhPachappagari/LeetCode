s = 'III'
conv = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}
i = 0
res = 0
while i<len(s):
    if (i+1)<len(s) and conv[s[i]] < conv[s[i+1]]:
        res += conv[s[i+1]]-conv[s[i]]
        i += 2
    else:
        res += conv[s[i]]
        i += 1
print(res)