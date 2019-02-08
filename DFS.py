import  re
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        return


def insert_elements(input_sequence, root, index):
    length_of_sequence = len(input_sequence)
    if index < length_of_sequence:
        temp_root = Node(input_sequence[index])
        root = temp_root
        root.left = insert_elements(input_sequence, root.left, 2 * index + 1)
        root.right = insert_elements(input_sequence, root.right, 2 * index + 2)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print (root.data)
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print (root.data)


def preorder(root):
    if root:
        print(root.data),
        preorder(root.left)
        preorder(root.right)


input_sequence = re.split(r'[;,\s]\s*', input("enter the list of numbers"))
root = None
root = insert_elements(input_sequence, root, 0)
print("\npreorder traversal\n")
preorder(root)
print ("\ninorder traversal\n")
inorder(root)
print ("\npostorder traversal\n")
postorder(root)
