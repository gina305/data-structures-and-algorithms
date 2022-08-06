class BinaryTree:
    """
    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    - pre order
    - in order
    -post order which returns an array of the values, ordered appropriately.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left == None:
            self.left = BinaryTree(value)
        else:
            node_data = BinaryTree(value)
            node_data.left = self.left
            self.left = node_data
        return self.left

    def insert_right(self, value):
        if self.right == None:
            self.right = BinaryTree(value)
        else:
            node_data = BinaryTree(value)
            node_data.right = self.right
            self.right = node_data
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
