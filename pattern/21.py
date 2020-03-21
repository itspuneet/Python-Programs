n=3
z=65
for i in range(n):
    k=z
    for j in range(n-i):
        print(' ',end='')
    for j in range(2*i+1):
        print(chr(k),end='')
        k-=1
    z=z+2
    print()
for i in range(1,n):
    c=z-4
    for j in range(i):
         print(' ',end='')
    for j in range((2*n)-2*i-1):
        print(chr(c),end='')
        c-=1
    z=z-2
    print()
