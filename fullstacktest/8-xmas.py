# # find number of operation to make an array adjecent is less than or equal to x
# # n=3 , x=3
# # list=[2,2,2]
# # out=1 exp =[2,1,2]

# def xmax(arr,x):
#     oper=0
#     res=[]    
#     mid= len(arr)//2
#     for i in range(1,len(arr)):
#         res.append((arr[i]+arr[i-1]))
#     if check(res,x):
#         return oper 
#     else:
#         oper+=1 
#         arr[mid]=arr[mid]-1 
#         # xmax(arr,x)
#         return oper+ xmax(arr,x)
# def check(list,x):
#     for n in list:
#         if n<=x:
#             return True 
#     return False     
        
# if __name__=='__main__':
#     # t=1 
#     # n=3 
#     list=[2,2,2]     
#     x=3
#     # k=0
#     print(xmax(list,x))

def xmax(arr,x):
    oper=0 
    res=[]
    mid= len(arr)//2 
    for i in range(1,len(arr)):
        res.append((arr[i]+arr[i-1]))
    for n in res:
        if n<=x:
            return oper 
        else:
            oper+=1 
            arr[mid]= arr[mid]-1 
            oper+ xmax(arr,x)
arr=[2,2,2]
x=3 
print(xmax(arr,x))
