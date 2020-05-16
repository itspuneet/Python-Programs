a='Hello#81@21349'
j=str()
z=0
for i in a:
    if  i.isnumeric():
        j+=i
print(j)
j=list(j)
for k in j:
    if not ord(k)%2==0:
        while i<len(j)-1:
            z=0
            while l<len(j)-i-1:
                if ord(a[z])>ord(a[z+1]):
                    t=a[z]
                    a[z]=a[z+1]
                    a[z+1]=t
        print(k,end='')
        
for i in j:
    if ord(i)%2==0:
        print(i,end='')

    
