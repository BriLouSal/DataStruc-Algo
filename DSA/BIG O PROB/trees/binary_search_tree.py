class TreeNodes:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self, value):
        # Remember if Node is (5) if the value is being sent to the value is les than self.value, we let it be left and else right
        if self.value < value:
            if self.left is None:
               self.left = TreeNodes(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNodes(value)
            else:
                self.right.insert(value)
            
            