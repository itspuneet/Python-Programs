a='what is your name'
a=list(a)
i=0
s=str()
c=-1
while i<len(a):
    if a[i]==' ':
        j=i-1
        while j>c:
            s+=a[j]
            j-=1
        c=i
        s+=' '
    if i==len(a)-1:
        j=i
        while j>c:
            s+=a[j]
            j-=1
    i+=1
print(s)
