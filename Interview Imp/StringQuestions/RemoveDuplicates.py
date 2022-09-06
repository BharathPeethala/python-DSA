from collections import Counter
if Counter('b') == Counter('d'):
    print("a==b")

str_in = "abccbccba"
while(True):
    n = len(str_in)
    i = 0
    temp = ""
    while(i < n):
        j = i+1
        while(j < n and str_in[i] == str_in[j]):
            j += 1
        if(j == i+1):
            temp += str_in[i]
        i = j
    if temp == str_in:
        print(str_in)
        break
    str_in = temp
