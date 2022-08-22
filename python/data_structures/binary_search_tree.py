class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
        
class BinaryTree:




    def __init__(self, root=None):
        self.root = root

    def pre_order(self):

        # empty list for values
        values = []

        def walk(root):
            if root is None:
                return
            if root:
                values.append(root.value)
                walk(root.left)
                walk(root.right)

        walk(self.root)
        return values

    def in_order(self):
        # left > root > right
        values = []

        if self.root == None:
            return

        def walk(node):
            if node:
                walk(node.left)
                values.append(node.value)
                walk(node.right)
        walk(self.root)
        return values

    def post_order(self):
        # left > right > root
        values = []

        if self.root == None:
            return

        def walk(node):
            if node:
                walk(node.left)
                walk(node.right)
                values.append(node.value)
        walk(self.root)
        return values

    def max_tree(self):

        if self.root == None:
            raise Exception('Sorry this Tree is currently empty')

        z = {'max_value': 0}

        def walk(node, z):
            if node:
                walk(node.left,z)
                walk(node.right,z)
                if node.value > z['max_value']:
                    z['max_value'] = node.value
        walk(self.root, z)
        return z['max_value']

class BinarySearchTree(BinaryTree):
    def add(self, value):
        def walk(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)
        walk(self.root)

    def contains(self, value):
        def walk(root):
            if root is None:
                return False
            elif root.value == value:
                return True
            elif value < root.value:
                return walk(root.left)
            else:
                return walk(root.right)
        return walk(self.root)

