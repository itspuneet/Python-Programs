n=3
for i in range(n):
    k=65
    for j in range(n-i):
        print(' ',end='')
    for j in range(2*i+1):
        print(chr(k),end='')
        k+=1
    print()
for i in range(1,n):
    c=65
    for j in range(i):
         print(' ',end='')
    for j in range((2*n)-2*i-1):
        print(chr(c),end='')
        c+=1
    print()
