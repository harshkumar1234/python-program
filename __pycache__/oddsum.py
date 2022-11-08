# find number of operation to make an array odd
# 1.operation for delete num and 2.operation for divide
# num=[6,6,10]
# out=2 

def oddsum1(num):
    oper= 0
    l=0 
    res=0
    r= len(num)
    while l<r:
        for i in num:
            res+=i 
        if res%2!=0:
            # return oper 
            print(oper)
            print("num is the break is ", num)
            break 
        # print(num)
        oper+=1
        del num[l]
        oper+=1
        for n in range(len(num)):
            num[n]= num[n]//2   
# l=0
num=[6,4,10]
print(num)
# del num[l]
# print(num)
print(oddsum1(num))
