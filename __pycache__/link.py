# def rearrange(arr, n):
#     max_id= n-1
#     min_id=0
#     max_elem= arr[n-1]+1
    
#     for i in range(0,n):
#         if i%2==0:
#             arr[i]+= ((arr[max_id]% max_elem) * max_elem)
#             max_id -= 1
#         else:
#             arr[i]+= ((arr[min_id]% max_elem) * max_elem)
#             min_id +=1
            
#     for i in range(0,n):
#         arr[i]= arr[i] / max_elem
        
# arr= [1,2,3,4,5,6,7,8,9]
# n=len(arr)
# print("this is original array")

# for i in range(0,n):
#     print(arr[i], end=" ")

# rearrange(arr, n)

# print("this is modified array" )

# for i in range(0,n):
#     print(int(arr[i]) , end=" ")


# this is lexicographic smallest order

# def printarr(arr,n):
#     for i in range(0,n):
#         print(arr[i] , end=" ")

# def smallest(arr, n):
#     arr.sort()
    
#     for i in range(0 , n-1, 2 ):
        
#          temp= arr[i]
#          arr[i]= arr[i+1]
#          arr[i+1]= temp
        
#     printarr(arr,n)

# # if __name__='__main__';
# # arr=[3,2,1,4,5]
# arr=[5,1,3,4,2]
# arr={5,1,3,4,2}
# # need of output - 2 1 3 2 5 4
# # output - 2 1 4 3 5 5 
# n=len(arr)
# smallest(arr,n)



#  second method for lexicographical order
# this is second problem of relevel test
# def gm(arr):
#     print(arr[0], "is number of white chocolate")
#     print(arr[1], "is weight of white chocolate")
#     print(arr[2], "is number of dark chocolate")
#     print(arr[3], "is wight of white chocolate")
#     print(arr[4],"kg", "Gru can lift ")
#     print(arr[5],"kg", "Minion can lift ")

#     wn1= int(input(" Gru enter the number of white chocolate "))
#     dn1= int(input("Gru enter the number of dark chocolate "))
#     a= (arr[1]* wn1) + (arr[3]* dn1)
#     if a<= arr[4]:
#         pass
#     else:
#         print("Gur can not lift")
    
#     wn2= int(input(" minion enter the number of white chocolate "))
#     dn2= int(input("Minion enter the number of dark chocolate "))
#     b= (arr[1]* wn1) + (arr[3]* dn1)
#     if a<= arr[5]:
#             pass
#     else:
#         print("minion can not lift")

#     print(" the tottal number of chocolate  which Gru and minion can loot from factory is ", 1, wn1+dn1+wn2+dn2)
  
  
  
  
  
  
    
# n=int(input("enter the number of rows"))
# for i in range(0 , n+1):
#     for j in range (1 , i+1):
#         # print(j , end=" ")
    
def printarr(arr,n):
    for i in range(0,n):
        print(arr[i] , end=" ")

def smallest(arr, n):
    # arr.sort()
    
    for i in range(0 , n+1 ):
        # arr.sort()
        for j in range( 1 , i+1):
          temp= arr[j]
          arr[j]= arr[j+1]
          arr[j+1]= temp
        
          printarr(arr,n)
        print(end=" ")


arr=[5,1,3,4,2]
# # need of output - 2 1 3 2 5 4
# # output - 2 1 4 3 5 5 
n=len(arr)
smallest(arr,n)
