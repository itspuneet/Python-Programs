def coprime(n,m=[]):
    f=[]
    for i in range(1,n+1):
        if n%i==0:
            f.append(i)
    m.append(f)
    return m
for i in range(1,int(input())+1):
    m=coprime(i)
k=[]
for i in m:
    if min(i)==1:
        print(i)
        
