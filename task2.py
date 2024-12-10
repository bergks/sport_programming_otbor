n = int(input())
maxk = int(input())
k = 0
for i in range(n-1):
    a = int(input())
    if a > maxk:
        k += maxk + 1
        maxk = a
    else:
        k += a + 1
k += 2
print(k)
