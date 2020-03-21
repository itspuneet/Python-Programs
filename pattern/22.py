n=5
z=65
for i in range(n):
    k=z
    for j in range(n-i):
        print(' ',end='')
    for j in range(i):
        print(chr(k),end='')
        k+=1
        c=k-2
    for j in range(i-1):
        print(chr(c),end='')
        c-=1
    print()
for i in range(2,n):
    k=65
    for j in range(i):
         print(' ',end='')
    for j in range(n-i):
        print(chr(k),end='')
        k+=1
        c=k-2
    for j in range(i):
        print(chr(c),end='')
        c-=1
    
    print()
