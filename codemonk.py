class codemonk:
    def check(n):
        C=list(map(int,input().split(' ')))[:n]
        L=list(map(int,input().split(' ')))[:n]
        m=min(C)
        i=1
        tot_cost=0
        while(i<n):
            tot_cost += L[i]*m
            i+=1
        print(tot_cost)
for i in range(int(input())):
    codemonk.check(int(input()))
