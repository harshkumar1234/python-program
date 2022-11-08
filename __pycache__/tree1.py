class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        
    def get_level(self):
        level=0
        p=self.parent 
        while p:
            level +=1
            p=p.parent 
        return level

    def print_tree(self):
        space=" "* self.get_level()*3
        prefix= space + " !_ _" if self.parent else " " 
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root=TreeNode("electronics")

    laptop=TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Surface"))
    
    cellphone=TreeNode("Cellphone")
    cellphone.add_child(TreeNode("I phone"))
    cellphone.add_child(TreeNode("Google pixel"))
    cellphone.add_child(TreeNode(" Vivo"))

    tv=TreeNode("TV")
    tv.add_child(TreeNode("Sumsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__=='__main__':
    root=build_product_tree()
    root.print_tree()
    pass