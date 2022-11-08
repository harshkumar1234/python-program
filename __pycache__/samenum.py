# # n=3
# # l=[2,1,2]
# # out=1

# def check(list):
#     for i in range(1,len(list)):
#         if list[i]==list[i-1]:
#             return True
#         # else:
#     return False
# def same(n,list):                       
#     oper=0
#     if check(list)==True:
#         return oper
#     # else:
#     # oper=oper+1
#     for i in range(len(list)):
#         if list[i]>1:
#             list[i]=list[i]-1
#         else:
#             continue
#     return same(n,list)
# n=3
# list=[2,1,2]
# # for i in range(len(list)):
# #     print(list[i])
# print(same(n,list))
    
def same(num):
    oper=0
    for i in range(1,len(num)):
        if num[i]==num[i-1]:
            return oper 
    oper+=1
    for i in range(len(num)):
        if num[i]>1:
            num[i]=num[i]-1
    return same(num)
num=[2,1,2]
print(same(num))