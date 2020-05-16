a='what is your name'
a=list(a)
i=0
j=0
k=0
s=str()
while i<len(a):
    if a[i]==' ':
        a[i-1]=ord(a[i-1])-32
        a[i-1]=chr(a[i-1])
        a[i+1]=ord(a[i+1])-32
        a[i+1]=chr(a[i+1])
    if i==0 or i==len(a)-1:
        a[i]=ord(a[i])-32
        a[i]=chr(a[i])
    i+=1
print(a)

for i in a:
    s+=i
    
print(s)
        
