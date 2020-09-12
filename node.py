class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()
