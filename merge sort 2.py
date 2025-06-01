def mergesort(arr):
    new_arr=[]
    length=len(arr)
    if(length<=1):
        return arr
    new_arr1=mergesort(arr[:length//2])
    new_arr2=mergesort(arr[length//2:])
    i=0;j=0
    while True:
        if(new_arr1[i]<new_arr2[j]):
            new_arr.append(new_arr1[i])
            i+=1
        else:
            new_arr.append(new_arr2[j])
            j+=1
        if(len(new_arr1)==i):
            new_arr=new_arr+new_arr2[j:]
            break
        elif(len(new_arr2)==j):
            new_arr=new_arr+new_arr1[i:]
            break
    return new_arr
print(mergesort([4,3,5,6,2,5,6,3,20,40,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))