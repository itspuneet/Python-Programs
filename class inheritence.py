class a:
    def a(s,k):
        s.k=k
        print("1st")
        print(k)
class b(a):
    def __init__(s,k):
        super().a(k)
        print("2nd")
        print(s)
k=b(5)
print(k.a())
