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
    
Noding=Node("19")
Noding2=Node("2")
Noding.next_node=Noding2
print(Noding.data)
print(Noding)
print(Noding.next_node.data)