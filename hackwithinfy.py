def p(a,n):
    a.sort()
    s=0
    for i in range(n):
        s+=a[i]
    a.append(s)
    print(max(a))
    
t=int(input())
n,m,a=[],[],[]
for i in range(t):
    n.append(list(map(int,(input()).strip().split(' '))))
    a.append(list(map(int,(input()).strip().split(' ')))[:n[i][0]])
for i in range(t):
    p(a[i],n[i][1])
    
