arr = list(range(1, 7))
print(arr)
maxi_element = 7
maxi_index = len(arr)-1
mini_index = 0
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] = arr[i]+(arr[maxi_index] % maxi_element)*maxi_element
        maxi_index -= 1
    else:
        arr[i] = arr[i]+(arr[mini_index] % maxi_element)*maxi_element
        mini_index += 1

for i in range(len(arr)):
    arr[i] = arr[i]//7

print(arr)
