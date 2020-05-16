t=int(input())
if t<1 or t>1000:
    exit()
else:
    n=[]
    for i in range(t):
        n.append(int(input()))   
    for i in n:
         print(sum(list(map(int,bin(i)[2:]))))
