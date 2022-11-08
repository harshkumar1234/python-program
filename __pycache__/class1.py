# class Human:
#     def __init__(self,n,r):
#         self.name=n
#         self.role=r
#     def do_work(self):
#         if self.role=='tennis':
#             print("my name is ",self.name)
#             print("my favourite game is ",self.role , "i want to do something in my life" )

#             # print(self.name,"")
#         elif self.role=='actor':
#             print("my name is ",self.name)
#             print("i like movies thats why i become a actor ",self.role)
#             print("i want to become a superman in my life  ")

#     def speek(self):
#         print(self.name," says hello how are you ?"," if you can think then you can do what you think  ")
    
# # saniya=Human("saniya",'tennis')
# # saniya.do_work()
# # saniya.speek()

# vivek=Human("vivek",'tennis')
# vivek.do_work()
# vivek.speek()

# akash=Human("akash",'actor')
# akash.do_work()
# akash.speek()

# # razz=Human("razz",'actor')
# # razz.do_work()
# # razz.speek()

# # ronaldo=Human("ronaldo","tennis")
# # ronaldo.do_work()
# # ronaldo.speek()

# class human:
#     def __init__(self,n ,r):
#         self.name=n
#         self.role=r
       
#     def do(self):
#         if self.role=="actor":
#             print("my name is ",self.name) 
#             print("i like movies thatswhy i become a actor ")
#             print("i hope you will be success in your life ")
#         elif self.role=='farmer':
#             print("my name is ", self.name)
#             print("i become farmer becouse my family background is very poor")
#             print("i prays to god you will crack relevel test")
#         else:
#             print("my name is ",self.name)
#             print("i am  ",self.role)
#             print("i wish to god you will become",self.role)
#     def speek(self):
#         print("i speek hindi ")


# harsh=human('harsh','actor')
# harsh.do(),harsh.speek()

# vivek=human('razz','farmer')
# vivek.do(),vivek.speek()

                # inheritance
# class vehicle:
#     def general_use(self):
#       print("general usage: transporation")

# class car(vehicle):
#     def __init__(self):
#         print("i am car")
#         self.wheels=4
#         self.has_roof=True
        
#     def specific_use(self):
#         print("specific usage: commute to work ,vocation  with family")

# class bike(vehicle):
#     def __init__(self):
#         print("i am bike ")
#         self.wheels=2
#         self.has_roof=False
#         print(" wheels" ,self.wheels)
#         print("has_ roof " ,self.has_roof)
#     def specific_use(self):
#         print("specific usage: road trip, racing")

# # make object and then call method
# car1=car()
# # c.general_use()
# # c.specific_use()

# # bike=bike()
# # bike.general_use()
# # bike.specific_use()

# # print(isinstance(car,car))
# # print(issubclass(car,vehicle))
# print(isinstance(car1,car))

        # multiple inheritance
# class father:
#     # def farmer(self):
#     def skills(self):
#         print("i am farmer but my son is software engineer")

# class mother():
#     # def wife(self):
#     def skills(self):
#         print("i am house wife but my son is going to crack relevel test")

# class child(father,mother):
#     # def boy(self):
#     def skills(self):
#         print("i am good student i am software engineer")

# harsh=child()
# # harsh.farmer()
# # harsh.wife()
# # harsh.boy()
# harsh.skills()

                #try and excep
# print("this is iteration function")
# num=[10,20,30,40,50]
# for a in num:
#     print(a)
# Memory=29
# try:
#     raise MemoryError("memory errors")
# except MemoryError as e:
#     print(e)

num=[10,20,30,40,50]
# print(dir(num))

# print("this is iteration")

# itr=iter(num)
# # print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# print("this reversed method")

# itr=reversed(num)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

