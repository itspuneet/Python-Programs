k=[]
for i in range(int(input())):
    l=[]
    n=int(input())
    a=list(map(int,input().split(' ')))[:n]
    for i in range(len(a)-1):
        b=(a[i:i+2])
        s=(int(bin(b[0])[2:]) and int(bin(b[1])[2:]))^(int(bin(b[0])[2:]) or int(bin(b[1])[2:]))
        l.append(s)
    print(l) 
    k.append(min(l))
for i in k:
    print(i)
