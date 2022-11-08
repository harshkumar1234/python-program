# list=[]
# while True:
#  num=int(input('''enter the number which you want to do--->  
#  1. push the element 
#  2. delete the element  
#  3. search the element  
#  4. display the element
#  5. break   '''))
#  if num == 1:
#      num1=int(input("enter the number which you want to push"))
#      list.append(num1)
#      print(list)
#  if num== 2:
#      if len(list)==0:
#          print("list is empty")
#      else:
#          list.pop() 
#          print(list)
#  if num==3:
#      num2=int(input("enter the number which you want to search")) 
#      if num2 in list:
#          print(num2)
#          print(list)
#      else:
#          print("number is not present in the list")
#  if num==4:
#      print(list)
#  if num==5:
#     break

# list=[]
# for a in range(0,11):
#     list.append(a)
#     print(list)
    # output is below
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list)
# list=[]
# for a in range(1,21):
#     list.append(a)
#     print(list)
# list=[ a for a in range(1,21) if a%2==0]
# print(list)
# table=[ a for a in range(1,101) if a%2==0]
# print(table)
# output - 0, 2, 4, 6, 8, 10]
queue=[]
while True:
 num=int(input('''enter the number which you want todo
    1.enter the number in the queue
    2.delete the number in the queue
    3. search number in the queue
    4. front number in queue
    5. rear number in queue
    6. break the program    '''))
    
 if num==1:
    num2=int(input("enter the number in the queue  "))
    queue.append(num2)
    print(queue)
    
 if num==2:
    if len(queue)==0:
        print("queue is empty")
    else:
        queue.pop()
        print(queue)
        
 if num==3:
    if len(queue)==0:
        print("queue is empty")
    else:
        num3=int(input("enter the number which you want to search"))
        if num3 in queue:
            print(num3)
            print(queue)
        else:
            print("number is not present in queue")
 if num==4:
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue[0])
        print(queue)
 if num==5:
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue[-1])
        print(queue)
 if num==6:
    print("thank you for playing ")
    break

# else:
#     print("aapne galat number dabaya hai")

