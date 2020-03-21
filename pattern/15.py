for i in range(5):
    k=65
    for j in range(4-i):
        print(' ',end='')
    for j in range(2*i+1):
        print(chr(k),end='')
        k+=1
    print()
