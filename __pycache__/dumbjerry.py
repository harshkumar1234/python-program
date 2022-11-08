# # n=3
# # list=[2,1,3]

# from audioop import reverse


# def dumb(n,list):
#     res=[]
#     list.sort(reverse=True)
#     size=len(list)-1
#     for i in range(0,len(list)):
#         print(list[i])
#         res.append(list.pop(i))
#         # res=list.remove(i)
#     return res 
# n=3
# list=[2,1,3]
# print(dumb(n,list))

from audioop import reverse


def dumb(arr):
    arr.sort()
    print(arr)
    res=[]
    for i in range(len(arr)):
        res.append(arr.pop())
    return res 
list=[2,1,3]
print("list is ", list)
print(dumb(list))
