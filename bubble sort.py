a=list(input('enter'))
i=0
j=0
s=str()
print(len(a))
while i<len(a)-1:
    j=0
    while j<len(a)-i-1:
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t  
        j+=1
    i+=1
print(a,end='')
a=set(a)
print()
for i in a:
    if  i.isdigit():
        s+=i
print(s)
