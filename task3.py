p, q = int(input()), int(input())

a, b, c = p,p,p
k = 0
while a <= q:
    while b <= q:
        while c <= q:
            if a+b <= c:
                break
            k += 1
            c += 1
        b += 1
        c = b
    a += 1
    b = a
    c = a
print(k)




    



    
    
    
        