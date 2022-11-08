# print a message on the screen
#print("this is my first program in python")

#to print our institute name
#print("government polytechnic aurai")

 #to display multiple statement
# print("hello how are you",)
# print("i am fine and you")
# print("i am also fine")

#to display a value of single variable
# a=10
# b=20
# print("the value of a is ",a)
# print("the value of b is ",b)
# # OR
#print(10,20)

 #to calculate the sum of two variable
# a=10
# b=20
# print("the value of sum  is ",a+b)
#OR
# print(10+20)

# #to calculate all arithmetic operations
# a=10
# b=20
# print("a=10 and b=20 ")
# print("the value of sum  is ",a+b)
# print("the value of sub  is ",a-b)
# print("the value of mul  is ",a*b)
# print("the value of div  is ",a/b)
# print("the value of mod  is ",a%b)

#to swap two variable using third varible
# a=10
# b=20
# print("before swapping a=10 and b= 20 ")
# c=a
# a=b
# b=c
# print("after swapping")
# print("a =",a, "b =",b)

#to initialize all data types
# a=10
# b=1.0
# c="harsh"
# print("int =",a ,"float = ", b ,"string = ", c)

#to input a number and display on the screen
# num=int(input("enter the number FIRST  " ))
# print(num ,"is given by you ")

#11 to input a two number and calculate them
# try:
    
#     num1=int(input("enter the number 1  "))
#     num2=int(input("enter the number 2  "))
#     oper=input("enter the operator +,-,*,/ ")
#     if oper == '+':
#         print("sum is ", num1+num2)
#     elif oper == '-':
#         print("sub is ", num1-num2)
#     elif oper == '*':
#         print("mul is ", num1*num2)
#     elif oper == '/':
#         print("div is ", num1/num2)
#     else:
#         print("you have entered wrong key")
# except:
#     print("please enter right number")

#12 swapping two variable using third variable
# try:
#     while True:
#         a=int(input("enter the first number  "))
#         b=int(input("enter the second number "))
#         print("before swapping ")
#         print("a is ",a , "b is ",b)
#         # using third variable
#         # c=a
#         # a=b
#         # b=c
 
#         #without using third variable
#         # a,b = b,a
#         # or 
#         print("after swapping ")
#         print("a is ",a , "b is ",b)
# except:
#     print("thank you ")


#13 to convert hours into minute and second
# while True:
#     hr=int(input("enter the hours "))
#     min=hr*60
#     sec=hr*60*60
#     print("hours is ", hr )
#     print("minute is ", min )
#     print("second  is ", sec )


#14 to convert years into month and day
# while True:
#     yr=int(input("enter the years "))
#     month=yr*12
#     day=yr*30
#     print("year  is ", yr )
#     print("month  is ", month )
#     print("day  is ", day )

#15 to calculate total and average marks of student
# name=input("enter your name ")
# sub1=int(input("enter number of subject 1  "))
# sub2=int(input("enter number of subject 2  "))
# sub3=int(input("enter number of subject 3  "))
# sub4=int(input("enter number of subject 4  "))
# sub5=int(input("enter number of subject 5  "))
# tot=sub1+sub2+sub3+sub4+sub5
# avg=tot/5
# if avg>= 90:
#     print(" A grade ")
# elif avg>= 70:
#     print(" B grade ")
# if avg>= 50:
#     print(" C grade ")
# else:
#     print(" fail  ", name)
# print("your name is " ,name)
# print(" your total number is " , tot)
# print(" your total avg is " , avg)

#16 to check whether the year is leap or not
# yr=int(input("enter the year"))
# if yr%4==0:
#     print("year is leap year ",yr)
# else:
#     print("year is not  leap year ",yr)

#17 to find the bigest number in two variable
# num1=int(input("enter the number 1 "))
# num2=int(input("enter the number 2 "))
# if num1>num2:
#     print("num1 is greater than num2 ", num1)
# elif num1<num2:
#     print("num2 is greater than num1 ", num2)
# else:
#     print("num1 is equal to the num2 ")

#18 to check the enter number is single digit or not
# num1=int(input("enter the number "))    
# if num1>0 and num1<9:
#     print("your number is single ",num1)
# elif num1==0:
#     print("your number is 0")
# elif num1<0:
#     print("this is  single digit ", num1 )
# else:
#     print("this is not single digit ", num1 )

#19 to check whether number is even or odd
# num=int(input("enter the number "))
# if num%2==0:
#     print("your number is even ", num)
# else:
#     print("your number is not even ", num)


#20 to check the number is positive , negative or zero
# num=int(input("enter the number "))
# if num>0:
#     print("number is positive " ,num)
# elif num<0:
#     print("number is negative ",num)
# elif num==0:
#     print("your number is zero ")
# else:
#     print("thank you ")

#21 find the highest number in three variable
# a=int(input("enter the number 1 "))
# b=int(input("enter the number 2 "))
# c=int(input("enter the number 3 "))
# if a>b and a>c:
#     print("1 is big ", a)
# elif b>a and b>c:
#     print("2 is big ", b)
# else:
#     print( "3 is big ", c)

#22 to check whether the character is vowel or consonant
# name=input("enter a alphabet ")
# if name == 'a' or name == 'A' :
#     print("this is vowel ",name)
# elif name == 'e' or name == 'E' :
#     print("this is vowel ",name)
# elif name == 'I' or name == 'i' :
#     print("this is vowel ",name)
# elif name == 'o' or name == 'O' :
#     print("this is vowel ",name)
# elif name == 'u' or name == 'U' :
#     print("this is vowel ",name)
# else:
#     print("this is consonant ", name)

#23 to calculate the grade of student
# name=input("enter your name ")
# sub1=int(input("enter first subject number"))
# sub2=int(input("enter second subject number"))
# sub3=int(input("enter third subject number"))
# sub4=int(input("enter four subject number"))
# sub5=int(input("enter five subject number"))
# tot=sub1+sub2+sub3+sub4+sub5
# avg=tot/5
# print(name)
# if sub1>40 and sub2>40 and sub3>40 and sub4>40 and sub5>40:
#     print("your total number is ",tot)
#     print("you passed ",avg )
# else:
#     print("you failed ",avg )
#     print("your total number is ",tot)

#24 to check whether letter is small ,capital ,digit,or special symbol
# let=input("enter the letter ")
# if let>='a' and let<='z':
#     print("letter is small",let)
# elif let>'A' and let<'Z':
#     print("letter is capital ",let)
# elif let>='0' and let<'9':
#     print("letter is digit ",let)
# else:
#     print("letter is special symbol ",let)

#25 to prints words corresponding number below 9
# print("please enter 1 to 9 number")
# num=int(input("enter the number "))
# if num is 1:
#     print("number is one  ",num)
# elif num is 2:
#     print("number is two",num)
# elif num is 3:
#     print("number is three",num)
# elif num is 4:
#     print("number is four",num)
# elif num is 5:
#     print("number is five",num)
# elif num is 6:
#     print("number is six",num)
# elif num is 7:
#     print("number is seven",num)
# elif num is 8:
#     print("number is eight ",num)
# elif num is 9:
#     print("number is nine ",num)
# else:
#     print("you have enter wrong key")

#26 to print day corresponding number
# print("please enter 1 to 9 number")
# num=int(input("enter the number "))
# if num==1:
#     print("monday")
# elif num==2:
#     print("tuesday")    
# elif num==3:
#     print("wednesday")    
# elif num==4:
#     print("thursday")    
# elif num==5:
#     print("friday")    
# elif num==6:
#     print("saturday")    
# elif num==7:
#     print("sunday")    
# else:
#     print("please enter right number")

#27 to print the message 10 times
# for a in range(0,11):
#     print("happy birthday to you ")

#28 to print 1 to 10 number
# for a in range (0,11):
#     print("this is ",a)

#29 to print 1 to 10 even number
# for a in range(1,20):
#     if a%2==0:
#         print("this is even",a)

#30 to print 1 to 10 odd number
# for a in range(1,20):
#     if a%2!=0:
#         print("this is odd ",a)

#31 to calculate sum of 10 natural number
# sum=0
# for a in range(0,11):
#     sum=sum+a
# print("sum of 10 natural number ",sum)    

#32 to calculate sum of even numbers below 10
# sum=0
# for a in range(1,11):
#     if a%2==0:
#         sum=sum+a
# print("sum of 10 even numbers is ",sum)
# #33 to calculate sum of odd numbers below 10
# sum=0
# for a in range(1,11):
#     if a%2!=0:
#         sum=sum+a
# print("sum of 10 odd numbers is ",sum)

#33 to print 1 to n numbers
# num=int(input("enter the numbers "))
# for a in range(1,num):
#     print("the number is ",a)

#34 to print 1 to n even numbers
# num=int(input("enter the number "))
# for a in range(1,num):
#     if a%2==0:
#         print("the number is even ",a)


#34 to print 1 to n odd numbers
# num=int(input("enter the number "))
# for a in range(1,num):
#     if a%2!=0:
#         print("the number is odd ",a)

#35 to calculate sum of 1 to n numbers
# num=int(input("enter the numbers "))
# sum=0
# for a in range(1,num+1):
#     sum=sum+a
# print("sum of n numbers is ",sum)

#36 to calculate 1 to n even numbers sum
# num=int(input("enter the numbers "))
# sum=0
# for a in range (1,num+1):
#     if a%2==0:
#         sum=sum+a
# print("sum of even numbers is ",sum)


#37 to calculate 1 to n odd numbers sum
# num=int(input("enter the numbers "))
# sum=0
# for a in range (1,num+1):
#     if a%2!=0:
#         sum=sum+a
# print("sum of odd numbers is ",sum)

#38 to calculate factorial of first five natural numbers
# fact=1
# for i in range(1,6):
#     fact=fact*i
# print("factorial of 5 numbers is ",fact)
# while True:
#  num=int(input("enter the number of factorial"))
#  fact=1
#  for a in range(1,num+1):
#     fact=fact*a
#     print(fact)
#  print("factorial of your number is ",fact)

#39 to print a table of 5
# for a in range(1,6):
#     # print("the table of ",a ,"------")
#     for b in range(1,11):
#         print(a,'*',b,'=',a*b )
#     # print("",end="")

# 40 to pyramid format star
# for a in range(0,6):
#     for b in range(0,a+1):
#         print("*",end="")
#     print(" ")
# ouptut 
# * 
# ** 
# ***
# ****
# *****
# ******

#41 to print pyramid format star
# for a in range(0,5):
#     for b in range(0,5):
#         if b>=4-a:
#             print("*", end="") 
#         else:
#             print(" ", end="")
#     print(" ")
# output
#     * 
#    ** 
#   ***
#  ****
# *****

# 42 to print pyramid format star
# for a in range(0,4):
#     for b in range(0,7):
#         if 3-a<= b <=3+a:
#             print("*", end="") 
#         else:
#             print(" ", end="")
#     print(" ")
# output 
#    *    
#   ***   
#  *****
# *******

# 40 to pyramid format star
# for a in range(1,6):
#     for b in range(1,a+1):
#         print( b ,end="")
#     print(" ")
    
#output
# 1 
# 12  
# 123 
# 1234
# 12345


