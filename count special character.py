a='t9@a42&516'
print(a)
a=list(a)
print(a)
c=0
for i in a:
    if not i>='a':
        c+=1
        print(i)
    if not i<='z':
        c+=1
        print(i)
print(c)
