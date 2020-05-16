a,b,c=list(map(int,input().split(',')))
k=[]
for i in range(c+1):
    if i%a==b:
        k.append(i)
if k:
    print(max(k))
else:
    print('-1')
