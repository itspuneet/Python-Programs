a='3,2,6,5,1,4,8,9'
list(a)
print(a)
s=0
c=0
k=''
five=a.index('5')
eight=a.index('8')
print(five,eight)
for i in a[::2]:
    c+=int(i)
for i in range(five,eight+1,2):
        s+=int(a[i])
        k+=a[i]
print('Num1=',c-s,'Num2=',k)

