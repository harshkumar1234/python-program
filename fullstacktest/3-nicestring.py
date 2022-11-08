# n=0100
# out=6 

def nices(arr):
    count=0 
    res=[]
    # arr= int(arr)
    for i in range(0,len(arr)+1):
        for j in range(i+1,len(arr)+1):
            # if arr[i]==1 or arr[j]==1:
            if  "1" in  arr[i:j] :
                count+=1 
                res.append((arr[i:j]))
            else:
                continue 
    return count 
    # return res 
arr="0100"
print('len(arr)',len(arr))
print("arr[0]", arr[0])
print(nices(arr))
