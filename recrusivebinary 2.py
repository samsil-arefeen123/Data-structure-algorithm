
def binary_search(list,target):
    low=0
    high=len(list)-1
    midpoint=(low+high)//2
    if(low>high):
        return None
    if list[midpoint]==target:
        return midpoint
    elif list[midpoint]>target:
        return binary_search(list[:midpoint],target)
    elif list[midpoint]<target:
        adder=midpoint+1
        return adder+binary_search(list[midpoint+1:],target)
def verify(index):
    if(index is not None):
        print("Yeee target found at index",index)
    else:
        print("Oops target not found")

list=[1, 5 ,6 ,10, 15,20]
verify(binary_search(list,20))