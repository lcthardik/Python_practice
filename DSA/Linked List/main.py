class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_end(self,data):
        new_node=node(data)
        new_node.next=None
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node

    def traverse(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
    
    def delete(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None   
                return
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next        
        if temp==None:
            return
        prev.next=temp.next
        temp=None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def detect_cyclic(self):
        fast=self.head
        slow=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                print("cyclic")
                return
        print("not cyclic")
    
    @staticmethod
    def merge(list1,list2):
        dummy=node(0)
        tail=dummy
        l1=list1.head
        l2=list2.head
        while l1 and l2:
            if l1.data>l2.data:
                tail.next=l2
                l2=l2.next
            else:
                tail.next=l1
                l1=l1.next
            tail=tail.next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        temp=linkedList()
        temp.head=dummy.next
        return temp
        
        

# TestList=linkedList()
# TestList.insert(3)
# TestList.traverse()
# TestList.insert(9)
# TestList.insert(3)
# TestList.insert(2)
# TestList.traverse()
# TestList.delete(9)
# TestList.traverse()
# TestList.insert_end(69)
# TestList.traverse()
# TestList.insert(69)
# TestList.traverse()
# TestList.reverse()
# TestList.traverse()


# TestList=linkedList()
# TestList.insert_end(1)
# TestList.insert_end(2)
# TestList.insert_end(3)
# TestList.insert_end(4)
# TestList.traverse()
# TestList.reverse()
# TestList.traverse()
# TestList.head.next.next.next.next=TestList.head.next
# TestList.traverse()
# TestList.detect_cyclic()

list1=linkedList()
list2=linkedList()
list1.insert_end(1)
list1.insert_end(3)
list1.insert_end(4)
list2.insert_end(2)
list2.insert_end(4)
list2.insert_end(6)
list1.traverse()
list2.traverse()
merged=linkedList.merge(list1,list2)
merged.traverse()
