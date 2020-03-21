k=0
for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    while k!=2*i-1:
        if k==0 or k==2*i-2:
            print('*',end='')
        else:
            print(' ',end='')
    
    print()
