f='11'
for i in range(5):
    c=1
    s=''
    for j in range(len(f)-1):
        if f[j]==f[j+1]:
            c+=1
        else:
            s=(str(c)+(f[j]))
        s=str(c)+(f[j])
    f=str(s)
    print(f)
