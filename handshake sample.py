a=[['1','2','3'],['1','5','1']]
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][0] not in a[i][j]:
            print(a[i][j])
    print()
