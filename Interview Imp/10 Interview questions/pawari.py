# cook your dish here
n = int(input())
pawri = 'pawri'
party = 'party'
length_party = len(party)
inputs = list()
for _ in range(n):
    inputs.append(input().strip())
print(inputs)
for i in inputs:
    if len(i) < len(party):
        print(i)
    else:
        res = ''
        print('entered')
        j = 0
        while(j < (len(i))):
            if i[j:j+length_party] == party:
                res += pawri
                j += length_party
            else:
                res += i[j]
                j += 1
        print(res)
