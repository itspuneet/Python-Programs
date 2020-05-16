n=int(input())
a=list(map(int,input().split()))[:n]
print(a)
b=list(map(int,input().strip().split()))[:n]
k=[]
for i in range(n):
    c=0
    while b[i]>0:
        b[i]-=a[i]
        c+=1
    if b[i]==0:
        k.append(c)
print(min(k))
