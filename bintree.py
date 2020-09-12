import node

class BinTree:
    root=None
    current=None
    def __init__(self,value):
        self.root=node.Node(value)
        self.current=self.root

    def addTree(self,value):
        if self.current.value:
            if value<self.current.value:
                if self.current.left==None:
                    self.current.left=node.Node(value)
                    self.current=self.root
                else:
                    self.current=self.current.left
                    self.addTree(value)
            elif value>self.current.value:
                if self.current.right==None:
                    self.current.right=node.Node(value)
                    self.current=self.root
                else:
                    self.current=self.current.right
                    self.addTree(value)
        else: self.current.value=value


x=BinTree(10)
x.addTree(9)
x.addTree(11)
x.addTree(12)
x.addTree(13)
x.addTree(15)
x.addTree(7)
x.addTree(14)
x.addTree(20)
x.addTree(8)
x.addTree(5)
x.addTree(17)
x.root.PrintTree()


