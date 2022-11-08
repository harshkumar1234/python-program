# arr=[5,1,4,3,2]
# out=2 

# def dominant(arr):
#     size= len(arr)
#     list=[]
#     oper=0 
#     for i in range(len(arr)):
#         num= arr.pop()
#         for j in range(1,len(arr)+1):
#             if num+j>arr[j]:
#                 oper+=1
#                 break 
#             else:
#                 continue 
#         arr.append(num)
#     return oper 
# arr=[5,1,4,3,2]
# print(dominant(arr))
# def dominant(arr):
#     size=len(arr)
#     oper=0 
#     for i ,n in enumerate(arr):
#         dom= arr.pop(i)
#         if dom is True :
#             oper+=1
#         arr[dom]= i 
#     return oper 
# def check(arr):
#     for j in range(len(arr)):
#         if dom+j>=arr[j]:
#                  return True 
#         else:
#                 return False 

def dominant(arr):
    size=len(arr)
    res=[]
    for i in range(len(arr)):
        num= arr.remove(i)
        res.append(num)
        
    print("res is ", res)
        # for j in range(len(arr)):
        # arr[num]=i 
            # arr.push(num)
    return arr 


arr=[5,1,4,3,2]
print(arr)
print(dominant(arr))
