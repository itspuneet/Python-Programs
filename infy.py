class node:
    def __init__(s,data):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s):
        s.root=None
        s.cur=None
    def append(s,data):
        temp=node(data)
        if s.root==None:
            s.root=temp
            s.cur=temp
            return
        s.cur.next=temp
        s.cur=temp
    def display(s):
        if s.root==None:
            print("no data")
            return
        temp=s.root
        while temp!=None:
            print(temp.data)
            tem==temp.next
