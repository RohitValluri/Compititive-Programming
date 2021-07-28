class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        new_node = Node(new_val)
        if (self.root == None):
            self.root = new_node
        else:
            present_node = self.root
            parent_node = self.root
            while (present_node != None):
                parent_node = present_node
                if (new_val < present_node.value):
                    present_node = present_node.left
                else:
                    present_node = present_node.right
            if (new_val < parent_node.value):
                parent_node.left= new_node
            else:
                parent_node.right = new_node
        pass

    def printSelf(self):
        # Your code goes here
        print(self.root)
        pass
        
    def search(self, find_val):
        # Your code goes here
        while self.root!=None:
            if self.root.value == find_val:
                return True 
            if self.root.value < find_val:
                self.root = self.root.right
            else:
                self.root = self.root.left
        return False
        pass

