def bayblade(n,a,b):
    a.sort()
    b.sort()
    c,i,k=0,0,0
    while i<len(a):
        j=k
        while j<len(b):
            if a[i]>b[j]:
                k=j+1
                c+=1
                break
            j+=1
        i+=1
    return c
t=int(input())
n,a,b=[],[],[]
ans=[]
for i in range(t):
    n.append(int(input()))
    a.append(list(map(int,input().strip().split(' ')))[:n[i]])
    b.append(list(map(int,input().strip().split(' ')))[:n[i]])
for i in range(t):
    ans.append(bayblade(n[i],a[i],b[i]))
for i in range(len(ans)-1):
    print(ans[i])
print(ans[len(ans)-1],end='')

