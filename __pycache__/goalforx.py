# # find the xth smallest element of the array A, which is equal to the mean of the array
# # n=3 , x=2
# # input: num=[1,3,1]
# # out=1  this is operation number  
# # explan= mean=(1+3+2)//3=2

def goalx(list,x):
    size=len(list)
    oper=0
    l=0
    r=size-1
    while l<r:
        temp= list[size-1]     
        list[size-1]= list[size-1]+1
        oper+=1
        if sum(list)//3==x:
            break
        else:
            goalx(list,x)
    return oper 
num=[1,3,0]
x=2
print(goalx(num,x))

