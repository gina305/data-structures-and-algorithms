class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t
        return self.left

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t
        return self.right

    # def get_left(self):
    #     return self.left

    # def get_right(self):
    #     return self.right

    # def set_left(self, tree):
    #     self.left = tree

    # def set_right(self, tree):
    #     self.right = tree

    # def set_data(self, data):
    #     self.data = data

    # def get_data(self):
    #     return self.data
