# t=2
# n1=10 , x1=6
# list1= [7,1,8,2,7,6,4,1,9,1]
# n2=4  , x2=7
# list2=[9,7,4,7]
from ast import BoolOp


def boot(list,x):
    set1=set()
    oper=0
    for i in range(0,len(list)):
        for j in range(1,len(list)):
            if i>=len(list) or j>=len(list):
                break
            # else:
            i+=1
            j+=1
            if list[i]>=x and list[j]>=x:
                # set1.add(i,j)
                oper+=1
            i=j+1
            j+j+2
            # i+=1
            # j+=1
    print(oper) 
def bootcam(t,n1,x1,list1,n2,x2,list2):
    boot(list1,x1)
    boot(list2,x2)

if __name__=='__main__':
    t=2
    n1=10 
    x1=6
    list1= [7,1,8,2,7,6,4,1,9,1]
    n2=4 
    x2=7
    list2=[9,7,4,7]
    bootcam(t,n1,x1,list1,n2,x2,list2)


