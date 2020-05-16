a=['9','8','7','6','5']
i=0
j=0
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
