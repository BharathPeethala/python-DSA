def intToRoman(num):
    romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for roman in romans:
        while num >= roman:
            res += romans[roman]
            num -= roman
    return res


print(intToRoman(1243))
