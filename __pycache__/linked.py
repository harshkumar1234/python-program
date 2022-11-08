# class Node:
#     def __init__(self,data=None,next=None):
#        self.data=data
#        self.next=next

# class linked_list:
#     def __init__(self):
#         self.head=None
        
#     def insert(self,data):
#         node=Node(data,self.head)
#         self.head=node
#     def print1(self):
#         if self.head is None:
#             print("linked list is empty")
#             return
#         itr=self.head
#         liststr=""
#         while itr:
#             liststr+= str(itr.data) +"--->"
#             itr=itr.next
#         print(liststr)

        
# # if __name__="__self.Name__":
# if __name__ == '__main__':
#     list=linked_list()
#     list.insert(10)
#     list.insert(20)
#     list.insert(30)
#     list.insert(40)
#     list.insert(50)
#     list.print1()

# this is Node class        
class Node:
    # this is method
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class linked_list:
    def __init__(self):
        self.head=None
        
    def insert_at_begin(self,data):
        node=Node(data,self.head)                
        self.head=node
    
    def insert_at_end(self,data):
        # if self.head is None:
            # self.head=Node(data,None)    
        node=Node(data,self.head)                
        self.head=node
        return
        iterate=self.head
        while iterate:
            iterate=iterate.next
            
        iterate.next=Node(data,None)
    def print2(self):
        if self.head is None:
            print("linked list is empty")
            return
        iterate=self.head
        list=""
        while iterate:
            # list =list + str(iterate.data)
            list += str(iterate.data) +"--->"
            iterate=iterate.next
           
        print(list) 
        
if __name__ == '__main__':
    
 li=linked_list()
#  li.insert_at_begin(38)
#  li.insert_at_begin(36)
#  li.insert_at_begin(34)
#  li.insert_at_begin(30)
 li.insert_at_end(50)
 li.insert_at_end(70)
 li.insert_at_end(90)
 li.print2()