# given a array a , and you have to fill array b but array b<=array a
# 3
# num=[2,3,1]
# out=5 sum of arrb= [2,2,1]

def fillarray(n,list1):
    list2=[0]*n
    for i in range(1,n):
        for j in range(len(list1)):
            if i<=list1[j]:
                list2[j]=i
    size=len(list2)
    print(list2)
    res=0
    for i in list2:
        res+=i
    return res 
num=[2,3,1]
n=3
print(fillarray(n,num))

