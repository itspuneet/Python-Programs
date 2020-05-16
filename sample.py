a=list(map(int,input().strip().split(' ')))
b=list(map(int,input().strip().split(' ')))
a.sort()
b.sort()
print(a)
print(b)
c=0
i=0
k=0
while i<len(a):
    j=k
    while j<len(b):
        print(i,j)
        if a[i]>b[j]:
            k=j+1
            c+=1
            break
        j+=1
    i+=1
print(c)
