a=list(input().split(','))
st,num=[],[]
for i in a:
    s1,n=i.split(':')
    st.append(s1)
    num.append(n)
print(st)
print(num)
for i in range(len(num)):
    for j in range(i):
        print(st[j])
    
