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
        """adding number before"""
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def popbefore(self):
        """removing number from lastest one"""
        current=self.head
        self.head=current.next_node
        return current.data


p=linkedlist()
print(p.is_empty())
p.addbefore(4)
print(p.is_empty())
p.addbefore(10)
p.addbefore(15)
print(p.size())
print(p.popbefore())
print(p.size())
print(p.popbefore())
print(p.popbefore())
print(p.is_empty())