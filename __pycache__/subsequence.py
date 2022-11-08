# n=4
# list=[1,2,1,3]
def sub(list,n):
    res=0
    list1=[]
    for i in range(len(list)-1):
        for j in range(i+1,len(list)-1):
            # list1.append(list[i][j])
            list1+=list[i][j]
            j+=1
            res+=1
        i+=1
    # return res 
    return list1
n=4
list=[1,2,1,3]
print(sub(list,n))