a='abcd@12#ef$k'
i=0
l=[]
s=[]
while i<len(a):
    if a[i].isalnum():
        l.append(a[i])
    else:
        s.append(a[i])
    i+=1
print(l)
print(s)
i=0
k=len(a)
m=0
while i<len(a):
    if a[i].isalnum():
        print(l[k],end='')
        k-=1
    else:
        print(s[m],end='')
        m+=1
    i+=1
