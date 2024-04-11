class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrder(root):
    stack1 = []
    stack2 = []
    stack1.append(root)
    if not root:
        return
    while len(stack1) > 0:
        curr = stack1.pop()
        stack2.append(curr.data)
        if curr.left is not None:
            stack1.append(curr.left)
        if curr.right is not None:
            stack1.append(curr.right)
    # print(stack2)
    while len(stack2) > 0:
        curr = stack2.pop()
        print(str(curr) +" ", end="")


if "__main__" == __name__:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    postOrder(root)
