def prime(n):
    f=0
    for i in range(2,n//2+1):
        if n%i==0:
            f=1
    if f==0:
        return (n)
p=[]
for i in range(2,int(input())+1):
    if prime(i)==None:
        pass
    else:
        p.append(prime(i))
print(p)
k={}
for i in range(len(p)):
    s=0
    l=0
    for j in range(i+1,len(p)-1):
        s+=p[j]
        if p[i]+s in p:
            k[p[i]]=p[i]+s
print(k{0})
for i in k:
    print(i)
