class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)





class BinaryTree:
    def __init__(self, data):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end= '')
            self.inorder_traversal(node.left)
        print(node, end='')
        if node.right:
            self.inorder_traversal(node.right)
            print(')', end='')


if __name__ == "__main__":
        tree = BinaryTree(7)
        n1 = Node('i')
        n2 = Node('s')
        n3 = Node('c')
        n4 = Node('b')
        n5 = Node('-')
        n6 = Node('/')
        n7 = Node('c')
        n8 = Node('d')
        n9 = Node('e')

        n6.left = n7
        n6.right = n8
        n5.left = n6
        n5.right = n9
        n3.left = n4
        n3.right = n5
        n2.left = n1
        n2.right = n3

        tree.root = n2
        tree.inorder_traversal()
        print('')

