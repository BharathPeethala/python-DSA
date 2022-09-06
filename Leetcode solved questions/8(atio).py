s = '4193 with words'
strInt = ''
sign = ''
for i in s:
    if i is '-' or i is '+' or (i <= '9' and i >= '0'):
        strInt += i
strInt = int(strInt)
print(strInt)
print(strInt if strInt > -2**31 and strInt < 2**31 else 0)
