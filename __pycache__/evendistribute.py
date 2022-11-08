# find evendistribute number
# def evendistribute(n1,n2):
#     list1=[]
#     list2=[]
#     for num in range(len(n1)):
#         list1.append((n1[num]))
#     for i in range(0,len(list1) , 2):
#         num1= (list1[i]+list1[i+1])%2
#     if num1==0:
#         print("yes")
#     else:
#         print("no")
#     for num in range(len(n2)):
#         list2.append((n2[num]))
#     for i in range(0,len(list2) , 2):
#         num2= (list2[i]+list2[i+1])%2
#     if num2==0:
#         print("yes")
#     else:
#         print("no")

# def evendist(t,n1,n2,list1,list2):
#     res=0
#     res1=0
#     for num in range(0,len(list1),2):
#         res=(list1[num]+list1[num-1])%2
#         if res==0:
#             print("yes")
            
#     i=0
#     while i<len(res):
#         if res[i]==0:
#             print("yes")
#         i+=1
#     for num in range(0,len(list2),2):
#         res1.append((list1[num]+list1[num-1])%2)
#     i=0
#     while i<len(res1):
#         if res1[i]==0:
#             print("yes")
#         i+=1
#     print("no")
# testcase=2
# n1=2
# n2=[2,4,1,3]
# m1=2
# m2=[10,12,2,3]
# print(n2, m2)
# # evendistribute(n2,m2)
# evendist(testcase,n1,m1,n2,m2)

def evendist(t,n1,list1,n2,list2):
    res1=0
    res2=0 
    for i in list1:
        res1+=i 
    if res1%2==0:
        print("YES")
    else:
        print("NO")
    for i in list2:
        res2+=i 
    if res2%2==0:
        print("YES")
    else:
        print("NO")
t=2 
n1=2
n2=2
list1=[2,4,1,3]
list2=[10,12,2,3]
evendist(t,n1,list1,n2,list2)

