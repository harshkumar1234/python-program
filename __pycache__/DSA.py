# # linked list 
# from distutils.log import error
# from itertools import count

# from pip import main


# class Node: #Node class here
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
    
# class linkedlist:   #linkedlist class here
#     def __init__(self):
#         self.head=None  #head variable
        
#     def insert_at_begin(self,data): #first method
#         node=Node(data,self.head)
#         self.head=node 
    
#     def insert_at_end(self,data): #second method
#         if self.head is None:
#             self.head=Node(data,None)
#             return
#         itr=self.head
#         while itr.next:
#             # list += str(itr.data) +"--->"
#             itr=itr.next
#         itr.next=Node(data,None)
        
#     def Print(self):  # third method print
#         if self.head is None:
#             print("linked list is empty")
#             return
#         itr=self.head
#         listr=""
#         while itr:
#             listr +=str(itr.data)+"---->"
#             itr=itr.next
#         print(listr)
        
#     def get_length(self):  #fourth method length
#         count=0
#         itr=self.head
#         while itr:
#             count +=1
#             itr=itr.next
#         return count
    
#     def remove_at(self,index):  #fivth method remove
#         if index<0 or index>self.get_length():
#             raise Exception ("invalid number")
#         if index==0:
#             self.head=self.head.next
#             return
#         count=0
#         itr=self.head
#         while itr.next:
#             if count==index-1:
#                 itr.next=itr.next.next
#                 break
#             itr=itr.next
#             count+=1
        
#     def insert_at_pos(self,index,data):  #sixth method insert in position
#         if index<0 or index>self.get_length():
#             raise Exception("invalid number")
#         if index==0:
#             self.insert_at_begin(data)
#             return
#         count=0
#         itr=self.head
#         while itr:
#             if count==index-1:
#                 node=Node(data,itr.next)
#                 itr.next=node
#                 break
#             itr=itr.next
#             count +=1
#     def insert_value(self,data_list):
#         self.head=None
#         for data in data_list:
#             self.insert_at_end(data)
            

        
# if __name__=='__main__':
#     # li= linkedlist()
#     # li.insert_at_begin(10)
#     # li.insert_at_begin(20)
#     # li.insert_at_begin(30)
#     # li.insert_at_begin(40)
#     # li.Print()
#     # output=40---->30---->20---->10---->
#     li=linkedlist()
#     # li.insert_at_end(10)            
#     # li.insert_at_end(20)            
#     # li.insert_at_end(30)            
#     # li.insert_at_end(40)            
#     # li.insert_at_end(50)            
#     # li.Print()
#     # output=10---->20---->30---->40---->50---->
    
#     li.insert_value([50,60,70,80,90])
#     li.Print()
#     #output=50---->60---->70---->80---->90---->
    
#     # print("length of linkedlist",li.get_length())
#     #output=length of linkedlist 5
    
#     li.remove_at(0)
#     li.Print()
    
#     # li.insert_at_pos(0,100)
#     # li.Print()
#     # output=100---->60---->70---->80---->90---->


#this is stack data structure
# from collections import deque

# class Stack:
#     def __init__(self):
#         self.container=deque() 
#     def Push(self,val):
#         self.container.append(val)
#     def pop(self):
#         self.container.pop()
#     def peek(self):
#         return self.container[-1]
#     def is_empty(self):
#         return len(self.container)==0
#     def size(self):
#         return len(self.container)
#     def Print(self):
#         print(self.container)
    
# if __name__=='__main__':
#     s=Stack()
#     s.Push(10)
#     s.Push(20)
#     s.Push(30)
#     s.Push(40)
    
#     s.Print()
#     # print("length of stack is",s.size())
#     # s.pop()
#     # s.Print()
#     # print(s.is_empty())
#     # s.Print()
#     # print(s.peek())
#     s.peek()

#this is queue data structure
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.container=deque()
#     def enqueue(self,val):
#         self.container.append(val)
#     def dequeue(self):
#         self.container.pop()
#     def is_empty(self):
#         return(self.container)==0
#     def size(self):
#         print("length of queue is ",len(self.container))  
#     def Print(self):    
#         print((self.container))

        
# q=Queue()          
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# q.enqueue(60)
# q.enqueue(70)
# q.Print()
     