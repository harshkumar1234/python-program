# n=2 
# arr=[2,3]
# out=4

def numberofarr(n,arr):
    oper=0
    barr=[]
    for i in range(1,n+1):
        for j in range(1,n+2):
            if i==j:
                continue 
            if i<j:
                barr.append([i,j])
                oper+=1 
            if i>j:
                barr.append((i,j))
                oper+=1 
    print(barr)
    return oper 
if __name__=='__main__':
    num=2 
    list=[2,3]
    print(numberofarr(num,list))
 
