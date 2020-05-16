s='1111122223334445556666'
i=0
n=len(s)-1
f=0
while i<n:
    j=0
    while j<n:
        if s[i]==s[j+1]:
            f=1
            break
        j+=1
    if f==1:
        print(s[i])
    i+=1
