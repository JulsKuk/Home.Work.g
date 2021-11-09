a = [160, 180, 173, 155]
a.sort(reverse=True)
X = int(input())
p = 0
while p < len(a) and a[p] >= X:
    p += 1

print(p + 1)
