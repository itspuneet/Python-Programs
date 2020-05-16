for i in range(2,10):
    flag=0
    s=0
    for j in range(2,i//2+1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        s+=i
        print('prime',i,s)
