n=int(input('enter'))
for i in range(1,n):
    k=65
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
