# from itertools import count
# from logging import exception
# from unicodedata import name


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def inser_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_value(self,datalist):
        self.head=None
        for data in datalist:
            self.inser_at_end(data)
            return

    def getlength(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count

    def remove_at(self,index):
        if index <0 or index> self.getlength():
            raise Exception("invalid number")
        if index==0:
             self.head=self.head.next
             return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_at_pos(self,index,data):
        if index <0 or index> self.getlength():
            raise Exception("invalid number")
        if index==0:
             self.insert_at_begin(data)
             return
        count=0
        itr=self.head
        while itr:
            if count== index-1:
                node=Node(data,None)
                itr.next=node
                break
            itr=itr.next
            count+=1
            
        # print(itr.data)
        

    def Print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        list=""
        while itr:
            suf=""
            if itr.next:
                suf='--->'
            list += str(itr.data)+ suf
            itr=itr.next
        print(list)

        
if __name__=='__main__':
    root=linkedlist()
    # root.inser_at_end(10)
    # root.inser_at_end(20)
    # root.inser_at_end(30)
    # root.inser_at_end(40)
    # root.insert_at_begin(10)
    # root.insert_at_begin(20)
    # root.insert_at_begin(30)
    # root.insert_at_begin(40)
    # root.insert_at_begin(50)
    # # root.Print()
    # print(root.getlength())
    # # root.insert_at_pos(6,100)
    # root.Print()
    # # root.remove_at(1)
    # root.Print()
    root.insert_value(['banana','apple','boll','bat'])
    root.Print()
