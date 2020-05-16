a='what is your name'
a=list(a)
i=0
s=str()
while i<len(a):
    if a[i]==' ':
        a[i-1]='#'
        a[i+1]='@'
    if i==0:
        a[i]='@'
    if i==len(a)-1:
        a[i]='#'
        
    i+=1
    
for i in a:
    s+=i
print(s)
    
