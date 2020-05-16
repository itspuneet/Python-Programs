def swap(a,X,B):
    I=[i for i in range(1,n+1)]
    a[X-1]=B
    k=[]
    for i in range(len(a)):
        c=0
        if a[i]!=i+1:
            for j in range(len(a)):
                if a[j]==i+1:
                    break
            k.append(a[j])
            c+=1
        else:
            k.append(a[i])
        print(k)
    if k!=I:
        for i in range(len(k)):
            if k[i]!=I[i]:
                k[i]=I[i]
                c+=1
    print(k,c)
    return a
n=int(input())
a=list(map(int,input().split(',')))[:n]
X,B=[],[]
N=int(input())
for i in range(N):
    (x,b)=(list(map(int,input().split(','))))
    X.append(x)
    B.append(b)
for i in range(N):
    a=swap(a,X[i],B[i])
