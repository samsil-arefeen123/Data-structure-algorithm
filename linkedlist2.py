class Node:
    next_node=None
    def __init__(self,data):
        #adding new data in the Node whenever its initialized
        self.data=data
    def print_data(self):
        #prints new data
        print(self.data) 
        
    def __repr__(self):
        return f"{self.data}"
class linkedlist:
    def __init__(self):
        self.head=None
    def addbefore(self,value):
        #adds a value before runs in O(1) time
        node=Node(value)
        temp=self.head
        self.head=node
        node.next_node=temp
    def popbefore(self):
        #removes a value at the top , runs in O(1) time
        p=self.head.data
        self.head=self.head.next_node
        return p
    def insert(self,index,data):
        #inserts in a specific index runs in linear or O(n) time
        n=self.head
        count=0
        if(index==0):
            self.addbefore(data)
            return None
        new_node=Node(data)
        while (n is not None):
            if(count+1==index):
                p=n.next_node
                n.next_node=new_node
                new_node.next_node=p
                break
            n=n.next_node
            count+=1
        return None
    def delete_by_index(self,index):
        #deletes by specific index runs in O(n) time
        if(index==0):
            self.popbefore()
            return None
        n=self.head
        count=0
        while (n is not None):
            if(count+1==index):
                if(n.next_node is not None):
                    n.next_node=n.next_node.next_node
                break
            count+=1
            n=n.next_node
    def search_by_index(self,index):
        # searches by index runs in O(n) time
        n=self.head
        while n is not None:
            if(index==0):
                return n.data
            index-=1
            n=n.next_node
        return "Nothing found"

    def __repr__(self):
        #prints all the value of linked list
        # runs in O(n) time
        li=[]
        
        node1=self.head
        while node1 is not None:
            if(node1==self.head):
                li.append(f'[Heads {node1.data}]')
            elif(node1.next_node==None):
                li.append(f'[Tails {node1.data}]')
            else:
                li.append(f'[{node1.data}]')
            node1=node1.next_node
        return ("->").join(li)
    

       
a=Node(5)
link=linkedlist()
link.addbefore(5)
link.addbefore(20)
print(link)
link.addbefore(20)
link.addbefore(50)
link.insert(4,40)
link.delete_by_index(1)
#print(link.popbefore())
link.delete_by_index(0)
print(link)
print(link.search_by_index(-1))