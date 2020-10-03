class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.start=None
    def insertLast(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def deleteFirst(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            self.start=self.start.next
    def viewList(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp = temp.next
list=linkedList()
list.insertLast(10)
list.insertLast(20)
list.insertLast(30)
list.insertLast(40)
list.viewList()
print()
list.deleteFirst()
list.viewList()