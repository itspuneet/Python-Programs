k=1
for i in range(1,6):
    for j in range(i):
        if k<10:
            print(k,end='')
            k+=1
            if k==10:
                print(1,end='')
        else:
            k=2
    print()
