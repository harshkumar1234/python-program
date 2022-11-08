# find unique number in the array
# input :
# 2
# 4
# 6 -1 2 6
# 3
# -1 2 3

def checkdup(list1):
    list=[]
    for i in list1:
        if i in list:
            return True
        else:
            list.append(i)
    return  False 

def uniq(list1):
    sub1=[]
    oper1=0
    minimum=0
    if checkdup(list1):
        list1.sort()
        max= list1[len(list1)-1]
        list1.pop(max)
        print(list1)
        for i in range(len(list1)):
            sub1.append(list1[i]-max) 
        oper1+=1
        uniq(list1)
    else:
        list1.sort()
        print(list1)
        minimum= list1[0]    
    return oper1 , minimum 
def uniquenum(t,n1,list1,n2,list2):
    if list1:
        print(uniq(list1))
    if list2:
        print(uniq(list2))

    
        
t=2
n1=4
list1=[6, -1 ,2 ,6]
n2=3
list2=[-1, 2, 3]
print(uniquenum(t,n1,list1,n2,list2))

    
            
            
        


# def unique(list1):
#     for i in range(len(list1)):
#         for j in range(i+1, len(list1)):
#             if list1[i]==list1[j]:
#                 return True
            
# # def uniquenum(testcase,num1,list1,num2,list2):
# def uniquenum(testcase,num1,list1):
#     if unique(list1):
        
#         # max1=0
#         # for i in range(len(list1)):
#         #     max1= max(max1, list1[i])
#         list1.sort()
#         max1= len(list1)
#         # del(list1[max])
#         big= list1.pop(max1-1)
#         # big= list1.remove(max1)
#         sublist=[]
#         count=0 
#         for i in range(len(list1)):
#             sub= list[i]-big 
#             sublist.append(sub)
#         count+=1
        
#         minnum=0
#         for i in range(len(sublist)):
#             minnum= min(minnum, sublist[i])
#         return (count, minnum)
#     else:    
#         minnum=0
#         count=0 
#         for i in range(len(sublist)):
#             minnum= min(minnum, sublist[i])
#         return (count , minnum )
    
    
    
# a=2
# b=4
# list=[6 ,-1, 2 ,6]
# print(uniquenum(a,b,list))



    # if unique(list2):
    #     max2=0
    #     for i in range(len(list2)):
    #         max2= max(max2, list2[i])
    #     # del(list1[max])
    #     big= list.pop(max)
    #     sublist=[]
    #     count=0 
    #     for i in range(len(list2)):
    #         sub= list[i]-big 
    #         sublist.append(sub)
    #     count+=1
        
    #     minnum=0
    #     for i in range(len(sublist)):
    #         minnum= min(minnum, sublist[i])
    #     return (count, minnum)
    # else:    
    #     minnum=0
    #     count=0 
    #     for i in range(len(sublist)):
    #         minnum= min(minnum, sublist[i])
    #     return (count , minnum )

# num= int(input("enter the number of test case"))
# while num>0:
#     num1= int(input("enter the number 1 "))
#     num2= int(input("enter the number  2"))
#     num-=1
# list1=[]
# list2=[]
# while num1>0:
#     list1.append(int(input("enter the digit in the list1")))
#     num-=1
# while num2>0:
#     list2.append(int(input("enter the digit  in the list2")))
# list1.sort()
# for i in range(len(list1)):
#     if list1[i]==list1[i-1]:            
#         # max1= del.(list1[len(list1)-1])
#         max1= list1.remove(len(list1)-1)



    
            
        
        
        