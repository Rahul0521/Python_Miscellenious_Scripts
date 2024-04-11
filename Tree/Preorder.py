class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return self.data


# Recursive Approach
def inorder(root):
    if root:
        
        inorder(root.left)
        print(str(root.data) + "", end=" ")
        inorder(root.right)
        


if "__main__" == __name__:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    inorder(root)
