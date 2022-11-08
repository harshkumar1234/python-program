# class Myclass:
#     num1=10
#     num2=20
#     print(num1,num2)
#     print("harsh")
#     def name(self,name):
#         self.name=name
#         print("harshit")
#         print("my name is " +self.name)

#         print("this is name function")

#         # print("my name is ",(self.name))

# obj1=Myclass()
# # obj1.name("ram")
# obj1.name("razz kumar upadhyay")
# obj1.name()
        
# class variable and instance variable
# from typing_extensions import IntVar


# class Myclass:
#     var=10
#     var1=20
#     # def_ _init_ _(self, invar):
#     # defx.intersection(y)
#     def __init__(self,invar): 
#         self.invar =invar
# obj1=Myclass("ram")
# obj2=Myclass("shaym")

# print(obj1.invar) 
 # we can access class variable with help of class name and object name
# print(Myclass.var)
# print(Myclass.var1)
# print(obj1.var)
# print(obj2.var1)
# print(obj1.invar)
# print(obj2.invar)
# print(invar)

# changing class variable to instance variable

from os import name


# class myclass:
#     num1=10
#     num2=20
#     # def__init__(self,name):
#     #     self.name=nam
#     def __init__(self,name):
#         self.name=name
#         # self.fathername=fathername
# obj1=myclass("ram")
# # print(obj1.num1)
# print(obj1.num2)
# print(myclass.num2)
# print(myclass.num1)
# obj2=myclass("harsh")
# print(obj1.name)
# print(myclass.name)
# myclass.var1=30
# obj1.name="vivek"
# #after changing
# print(myclass.var1)
# print(obj1.name)

#example of inheritance in python
# class imployee:
#     def set1(self,empid,name,salary):
#         self.empid=empid
#         self.name=name
#         self.salary=salary
# class fitness(imployee):
#     def set2(self,height,weight):
#         self.height=height
#         self.weight=weight

#     def display(self):
#       print("imployee id is",self.empid)
#       print("name is ",self.name)
#       print("salaarya is ",self.salary)
#       print("height is ", self.height)
#       print("weight is ",self.weight)

# obj1=fitness()
# # obj2=imployee()
# obj1.set1(1,"harsh",60000)
# obj1.set2("6 feet",55)
# obj1.display()
# # obj2.display()
# class imployee:
#     print("this is classs variable function (print)")
#     def set1(self,impid,name,salary):
#         self.impid=impid
#         self.name=name
#         self.salary=salary
#         print("this is set1 function")
# class fitness(imployee):
#     print("this is fitness class variable (print)")
#     def set2(self,height,weight):
#         self.height=height
#         self.weight=weight
#         print("this is set2 function")
#     def display(self):
#         print("imployee id is ",self.impid)
#         print("name is ",self.name)
#         print("salary is ",self.salary)
#         print("height is ",self.height)
#         print("weight is ",self.weight)
#         print("this is display function")

# # obj1=imployee()
# obj2=fitness()
# obj2.set1(1,"harsh",60000)
# obj2.set2("6 feet",60)
# obj2.display()
# obj3=fitness()
# obj3.set1(2,"harshit",50000)
# obj3.set2("5feet",50)
# obj3.display()

# issubclass and isinstanceclass
# class myclass:
#     pass
# class fitness(myclass):
#     pass
# obj1=myclass()
# obj2=fitness()

# print(issubclass(myclass,fitness)) # output false
# print(issubclass(fitness,myclass))  #output true
# print(issuperclass(myclass,fitness))
# print(isinstance(obj1,myclass)) #output true
# # print(isinstance(myclass,obj1)) # errror
# print(isinstance(obj1,fitness))  #output false
print(2.3-2.0)