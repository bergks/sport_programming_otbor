import time
n = int(input())
st = 0
su = []
maxraz = 0
for i in range(n):
    st += int(input())
    su.append(st)
last = su[-1]
for i in range(n-1):
    traz = abs(2*su[i] - last)
    maxraz = max(traz, maxraz)
print(maxraz)
