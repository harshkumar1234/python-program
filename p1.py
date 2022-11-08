# import heapq
# list=[1,3,5,2,4,6]
# heapq.heapify(list)
# print(list)
# heapq.heappushpop(list,9)
# print(list)

def bubblesort(list):
    for num in range(len(list)-1,0,-1):
        for idx in range(num):
            if list[idx] > list[idx+1] and list[idx-1] < list[idx]:
                temp= list[idx]
                list[idx]= list[idx+1]
                list[idx+1]= temp
                
                
                
# list = [19,2,31,45,6,11,121,27]
list=[5,1,3,4,2]
bubblesort(list)
print(list)



