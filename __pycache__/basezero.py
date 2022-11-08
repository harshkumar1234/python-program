# t=1
# n=3
# num=[2,1,2]
# out=1  bcz[1,1,1]
def samenum(list):
    size=len(list)
    res=[0]*size
    oper=0
    for i in range(size):
        if list[i]>1:
            list[i]=list[i]-1
            res[i]=list[i]
        else:
            res[i]=list[i] 
    oper+=1
    l=0
    r=len(res)-1
    while l<r:
        if res[l]==res[r]:
            break 
        else:
          samenum(list)  
    return oper 
            
                  
# num=[3,2,3]
num=[2,1,2]
print(samenum(num))
