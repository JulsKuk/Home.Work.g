a = [1, 3, 5, 4, 3, 5, 3, 1]
b = 0
for i in range(1, len(a) - 1):
    if  a[i] > a[i - 1] and  a[i] > a[i +1]:
        b += 1

print(b)