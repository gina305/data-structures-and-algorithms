from data_structures.binary_tree import BinaryTree

def create_tree():
    tree = BinaryTree(2)

    print(tree.data)
    
class BinarySearchTree(BinaryTree):
    """
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add:
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.

Contains:
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.
    """

   
    def __init__(self, data=None):
        self.root = data
        self.left = None
        self.right = None
        self.value = "word"
        return self.root     
        
    def add(self, word):
        # if self.left == None:
        #     self.left = BinaryTree(word)
        # # else:
        # #     node_data = BinaryTree(value)
        # #     node_data.left = self.left
        # #     self.left = node_data
        # # return self.root
        # print(self.left)
        # return self.left
        word = word.split()

        return word

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
