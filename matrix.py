r=int(input('row'))
c=int(input('col'))
m=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(input())
    m.append(a)
for i in range(r):
    for j in range(c):
        print(m[i][j],end='')
    print()
for i in range(r):
    for j in range(c):
        if i==j:
            print(m[i][j],end='')
        else:
            print(' ',end='')
    print()
    
