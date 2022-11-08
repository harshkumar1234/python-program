from logging import root
import numbers
from xml.dom.minidom import Element


class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if self.data==data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)        
            else:
                self.right=BinaryTree(data)
        #in_order traversing
    def in_order_traversal(self):
        element=[]
        if self.left:
            element +=self.left.in_order_traversal()

        element.append(self.data)
        
        if self.right:
            element +=self.right.in_order_traversal()
        return element
    # search method
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
                
    # delete method
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
def Build_tree(element):
    root=BinaryTree(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

        
        
        
        
        
        
        
if __name__=='__main__':
    numbers=Build_tree([17,4,5,4,5,4,1,20,9,23,18,34])
    print(numbers.in_order_traversal())
    # output= [1, 4, 9, 17, 18, 20, 23, 34]
    # print(numbers.search(20))
    # numbers.delete(20)
    # remove 20
    # numbers.delete(200)
    #return none
    print(numbers.find_max())
    # output= 34
    print(numbers.find_min())
    # output =1
    # print(numbers.in_order_traversal())
