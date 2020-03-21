for i in range(5):
    for j in range(5-i-1):
        print(' ',end='')
    print('*',end='')
    for j in range(2*i-1+1):
        print(' ',end='')
        if i>0:
            print('*',end='')
        print()
