low=0
high=0
def recursive_binary(list,target):
    global low,high
    midpoint=(low+high)//2
    if(list[midpoint]==target):
        return midpoint
    elif(list[midpoint]<=target):
        low=midpoint+1
    else:
        high=midpoint-1
    if(low>high):
        return None
    return recursive_binary(list,target)
def verify(value):
    if value is not None :
        print("Target value found at index",value)
    else:
        print("Target value not found")
list=[1, 5 ,6 ,10, 15,20]
high=len(list)-1
verify(recursive_binary(list,4))