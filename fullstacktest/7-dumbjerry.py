# find dumb element in the array 
# n=3
# arr=[3,1,2]
# out= [3,2,1]

# def dumb(arr):
#     # minelem= min(arr)
#     res=[]
#     arr.sort()
#     for i in range(len(arr)):
#         res.append(arr.pop())  
#     return res 

# arr=[3,1,2]
# print(dumb(arr))

def dumb(arr):
    res=[]
    size=len(arr)
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                res.append(arr.remove(arr[j]))
            else:
                res.append(arr.remove(arr[i]))
    set(res)
    return res 
arr=[3,1,2]
print(dumb(arr))

