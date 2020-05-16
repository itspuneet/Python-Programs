class node:
    def __init__(s,data):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s):
        s.head=None
    def insert(s,data):
        temp=node(data)
        if(s.head):
            current=s.head
            while(current.next):
                current=current.next
            current.next=temp
        else:
            s.head=temp
    def print(s):
        current=s.head
        while(current):
            print(current.data)
            current=current.next
ll=linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.print()
