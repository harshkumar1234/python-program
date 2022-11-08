# 5
# 5 1 4  3 2
# output 2
#  5 4
# i1+i>i+1
# def dominantnum(n,arr):
#     num=[]
#     stack1=[]
#     count=0
#     for i in range(len(arr)):
#         for j in range(1,len(arr)):
#             num= arr.pop(i)
#             if arr[0]<arr[len(arr)-1]:
#                 while num+j>arr[i]:
#                     stack1.append(arr[i])
#                     if len(stack1)==4:
#                         count+=1
#                     else:
#                         # break
#                         continue
#             else:
#                 arr.reverse()
#                 while num+j>arr[i]:
#                     stack1.append(arr[i])
#                     if len(stack1)==4:
#                         count+=1
#                     else:
#                         # break
#                         continue
#     return count
def dominantnum(n,list):
    res=[]
    count=0
    for i in range(len(list)):
        num= list.remove(list[i])
        print(num)
        for j in range(1,len(list)):

            if num+j>list[j]:
                res.append(num)
                if len(res)==4:
                    count+=1
            else:
                break 
        list[i]= num 
    return count 
                 
n=5
list=[5,1 ,4  ,3 ,2]
print(dominantnum(n,list))
                
            

