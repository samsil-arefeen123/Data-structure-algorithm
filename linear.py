def linear_search (li,target):
    for i in range (len(li)):
        if(li[i]==target):
            return i
    return None
def verify(index):
    if (index==None):
        print("Target not found")
    else:
        print("Target found at ",index," position")
list=[1, 5 ,6 ,10, 15,20]
verify(linear_search(list,20))