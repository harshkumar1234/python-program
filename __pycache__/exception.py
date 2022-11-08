# while True:
#     print("write cencel for exit")

#     num=(input("enter the numebr   "))
#     try:
#       if num=='cencel':
#           break
    
#       elif num>10:
#           print("your number is greater than 10.   ")
#       else:
#           print("your number is less than 10    ")
#     except Exception as e:
#         print(f"you have enter  wrong button:{e}")
#         print(e)

# while True:
#     print("write cencel for exit")

#     num=(input("enter the numebr   "))
#     if num=='q':
#         break
#     try:
#         num=int(num)
#         if num>10:
#             print("your number is greater than 10.   ")
#         else:               
#             print("your number is less than 10    ")
#     except Exception as e:
#              print(f"you have enter  wrong button:{e}")
#              print(e)
while True:
    print("write cencel for q")

    num=(input("enter the numebr   "))
    if num=='q':
        break
    try:
        num=int(num)
        if num>10:
            print("your number is greater than 10.   ")
        else:               
            print("your number is less than 10    ")
    except :
             print(f"you have enter  wrong button:{e}")
            #  print(e)
