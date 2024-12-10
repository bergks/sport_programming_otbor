import math 
a, h, k, m, s = int(input()), int(input()), int(input()), int(input()), int(input())
 
n = 1
polosi = math.ceil(a / m)
t_rul = s
if k > h:
    polosirull = s // k
    n = math.ceil(polosi/polosirull)
else:
    for i in range(polosi):
        t_rul = t_rul - (math.ceil(h/k)*k)
        if t_rul < h:
            n += 1
            t_rul = s
print(n)
    
