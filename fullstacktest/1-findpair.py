# t=2 
# n=2
# arr=[2,4,1,3]
# n=2
# arr=[10,12,2,3]

def findpair(t,n1,list1,n2,list2):
    def check(arr):
        res1=[]
        for i in range(1,len(arr),2):
             res1.append((arr[i]+arr[i-1])) 
        print(res1)
        for i in res1:
            if i%2!=0:
               return ("NO")
        return ("YES")
    print(check(list1))
    print(check(list2))

t=2 
n1=2
arr1=[2,4,1,3]
n2=2
arr2=[10,12,2,3]
findpair(t,n1,arr1,n2,arr2)



         
