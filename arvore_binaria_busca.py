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

    def postorder_traversal(self, node= None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    def height(self, node= None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)


    def postorder_example_tree():
            tree = BinaryTree(7)
            n1 = Node('i')
            n2 = Node('n')
            n3 = Node('s')
            n4 = Node('c')
            n5 = Node('r')
            n6 = Node('e')
            n7 = Node('v')
            n8 = Node('a')
            n9 = Node('s')
            n0 = Node('e')

            n0.left = n6
            n0.right = n9
            n6.left = n1
            n6.right = n5
            n5.left = n2
            n5.right = n4
            n4.right = n3
            n9.left = n8
            n8.right = n7

            tree.root = n5
            return tree

    if __name__=="__main__":
        tree = postorder_example_tree()
        print("Percurso em pós ordem:")
        tree.postorder_traversal()
        print("Altura: ", tree.height())