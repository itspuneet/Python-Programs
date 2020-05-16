a=list(map(list,input().split(' ')))
b=int(ord(''.join(a[1]))-48)
for i in range(b):
    a[0][i]='9'
print(''.join(a[0]))
