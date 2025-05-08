def binary_search(li,target):
    low=0
    high=len(li)-1
    while (low<=high):
        midpoint=(low+high)//2
        if(li[midpoint]==target):
            return midpoint
        elif(li[midpoint]>target):
            high=midpoint-1
        else:
            low=midpoint+1
    return None
def verify(value):
    if value is not None :
        print("Target value found at index",value)
    else:
        print("Target value not found")
list=[1, 5 ,6 ,10, 15,20]
verify(binary_search(list,11))