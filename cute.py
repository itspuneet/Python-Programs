def prime():
    f=0
    for a in range(100):
        for i in range(2,a//2):
            f=0
            if a%i==0:
                f=1
                print('not prime',a,i,end='')
                break
        if f==0:
            print('prime',a,i)
            
