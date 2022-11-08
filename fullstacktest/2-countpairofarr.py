# given a array find count of arr b 
# n=2 
# arr=[2,3]
# out= (1,2),(1,3),(2,1),(2,3)
def countpair(n,arr1):
    count=0 
    for i in range(1,n+1):
        for j in range(1,n+2):
            if i!=j  and i<j or i>j:
                count+=1 
                print([i,j])
            else:
                continue 
    return count 
                
n=2 
arr=[2,3]
print(countpair(n,arr))
