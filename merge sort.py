def merge (li):
    if(len(li)==1):
        return li
    if(len(li)==2):
        if(li[0]>li[1]):
            li[0],li[1]=li[1],li[0]
        return li
    
    li1=merge(li[:len(li)//2])
    #print(li1,end=',')
    li2=merge(li[len(li)//2:])
    #print(li2)
    i=0
    j=0
    new_li=[]
    while(len(li)!=len(new_li)):
        if(j==len(li2)):
            new_li=new_li+li1[i:]
            #print(new_li)
            break
        elif(i==len(li1)):
            new_li=new_li+li2[j:]
            #print(new_li)
            break 

        if(li1[i]>li2[j]):
            new_li.append(li2[j])
            j+=1
        elif(li1[i]<=li2[j]):
            new_li.append(li1[i])
            i+=1
    #print(new_li)
    return new_li        

print(merge([10,5,2,100,45,56,4,3,2,4,5,3,5,6,4,3]))