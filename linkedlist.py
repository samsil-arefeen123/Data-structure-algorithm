class Node:
    """An object for storing single node of a linked list
    Models: two attributes data and the link to the next node in the list
    """
    data=None
    next_node=None
    def __init__(self,data):
        self.data=data
        pass
    def __repr__(self):
        return "Node data %d"%int(self.data)
class linkedlist:
    def __init__(self):
        self.head=None
        pass
    def __repr__(self):
        li=[]
        p=self.head
        c=0
        while p:
            if not c: 
                li.append (f"[Heads {p.data}]")
                c+=1
            elif not p.next_node:
                li.append(f"[Tails {p.data}]")
            else :
                li.append(f"[{p.data}]")
            p=p.next_node
        return "->".join(li) 
    def search(self,key):
        """It returns the object having the key at first
        Runs O(n) times """

        current=self.head
        while current:
            if current.data==key:
                return current
            current=current.next_node
        return current
    def insert(self,index,data):
        count=0
        current=self.head
        new_node=Node(data)
        if(index==0):
            self.head=new_node
            new_node.next_node=current
            return None
        while current:
            if(index==count+1):
                print("Enter or not")
                new_node.next_node=current.next_node
                current.next_node=new_node
                return None
            count+=1
            print(current)
            current=current.next_node
        return None
        
    def is_empty(self):
        return self.head==None
    def size(self):
        """Return the number of Nodes connected in the list"""
        count=0
        current=self.head
        while (current):
            count+=1
            current=current.next_node
        return count
    def addbefore(self,data):
        """adding number before takes O(1)"""
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def popbefore(self):
        """removing number from lastest one
        takes O(1) time"""
        current=self.head
        self.head=current.next_node
        return current.data
    def removebyindex(self,index):
        current=self.head
        if(index==0):
            self.head=self.head.next_node
            return None
        while index>1:
            index-=1
            current=current.next_node
        k=current.next_node
        current.next_node=k.next_node
        return None
  #  def removebykey(self,key):

p=linkedlist()
p.addbefore(145)
p.addbefore(7)
p.addbefore(5)
p.insert(2,10)
p.insert(0,4)
p.insert(3,6)
p.insert(10,6)
print(p)
p.removebyindex(5)
print(p)
#print(p)
"""print(p.is_empty())
p.addbefore(4)
print(p.is_empty())
p.addbefore(10)
p.addbefore(5)
p.addbefore(145)
p.addbefore(7)
print(p.search(145))
print(p.is_empty())
print(p)
"""