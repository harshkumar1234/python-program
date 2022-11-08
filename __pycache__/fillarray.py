# fill array 
# N=3
# list1=[3,2,1]
# find another maximum sum of list list2<=list1
# list2=[1,1,0]
# list2=[2,2,1]
# output=5
def fillarray(N, list):
    temp=[]
    size=len(list)
    # for i in range(0,size):
    #     while i<=list[1]:
    #         temp.append(i)
    #         i+=1
    #     if len(temp)<3 and len(temp)>3:
    #         break
    # for j in range(1,size):
    #     while(j<=list[0]):
    #         temp.append(j)
    #         j+=1
    for i in range(0,size):
        for j in range(i):
            while j<=list[0]:
                temp.append(j)
                
            
            
            

    