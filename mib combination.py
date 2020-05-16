def perm(n,r):
    return fact(n)/fact(n-r)
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def permutation(a):
    n=a.index(a[0])+1
    print(n)
    r=len(a)
    print(r)
    p=perm(n,r)
    print(p)
    for i in range(r+1):
        t=a[i]
        a[i]=a[n]
        a[n]=a[i]
        permutation(a)
        t=a[i]
        a[i]=a[n]
        a[n]=a[i]
    print(a)

permutation(['m','i','b'])

