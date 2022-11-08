# count number of pair  from given arr
# t=2
# list=[2,3]
# out=4  exp = [1,2],[1,3],[2,3],[2,1]

def countlist(t,arr):
    list=[]
    count=0
    for i in range(1,len(arr)+1):
        for j in range(len(arr)+1):
            if i>=1 and j>=1 and i!=j:
                list+=[i,j]
                count+=1
            i+=1
            j+=1
    return count 
t=2
list=[2,3]
print(countlist(t,list))