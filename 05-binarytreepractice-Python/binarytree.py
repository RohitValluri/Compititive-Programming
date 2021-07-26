# from _typeshed import Self


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        
        
        

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        self = Node(self)
        if self.left:
            self.left.print_tree()
        print(self.value),
        if self.right:
            self.right.print_tree()
        # pass

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        # pass

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        
        pass
root = BinaryTree(15)
# print(root.search(4))
print(root.print_tree())