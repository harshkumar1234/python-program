# find maximum number of operation in the array
# n=3
# x=2
# list=[1,3,1]
# out=1 exp= (1+3+2)//3==2 IN 1 operation 

def goalx(arr,x):
    oper= 0 
    for i in range(1,len(arr)+1):
        oper+=1
        arr[len(arr)-1]=arr[len(arr)-1]+1
        if sum(arr)//3==x:
            # return oper 
            print("operation is ", oper)
            break
        else:
            continue
arr=[1,3,0]
x=2 
goalx(arr,x)
