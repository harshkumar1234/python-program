# find positive and negative number in the array 
# arr=5 , x=3 
# arr= [3,1,1,2,3]
# out= 3 different maximum number of balloon

def maxballoon(arr,x):
    oper=0 
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            oper+=1 
        else:
            continue 
    return oper+1 
            
arr= [3,1,1,2,3]
x=3 
print(maxballoon(arr,x))

