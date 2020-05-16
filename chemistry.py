a=list(map(int,input().split(',')))[:4]
x,y,p,q=a[0],a[1],a[2],a[3]
b1,b2,b3=1,1,1
print(b1,'C',x,b2,'H',y,',',b3,',C',p,'H',q)
print((b1*x+b2*y),(b3*(p*q)))
while (b1*x+b2*y)!=(b3*(p*q)):
    while b1*x!=b3*p:
        print('l1')
        if b1*x!=p:
            b1+=1
        elif x!=b3*p:
            b3+=1
        else:
            b1+=1
            b3+=1
    while b2*y!=b3*q:
        print('l2')
        if b2*y!=q:
            b2+=1
        elif y!=b3*q:
            b3+=1
        else:
            b2+=1
            b3+=1
print(b1,'C',x,b2,'H',y,',',b3,',C',p,'H',q)
