class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def get_root(self, node):
        if node is None:
            print('Empty BST')
        else:
            print(node.value)

    def insert(self, node, value=None):
        if self.root is None and value is None:
            self.root = node
        else:
            if node.value > value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.insert(node.left, value)
            elif node.value < value:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.insert(node.right, value)
            else:
                print('Value already exists')

    def print_inorder(self, root_node):
        # left --> root --> right
        result = []
        if root_node is not None:
            result += self.print_inorder(root_node.left)
            result.append(root_node.value)
            result += self.print_inorder(root_node.right)
        return result

    def print_preorder(self, root_node):
        # root --> left --> right
        result = []
        if root_node is not None:
            result.append(root_node.value)
            result += self.print_preorder(root_node.left)
            result += self.print_preorder(root_node.right)
        return result

    def print_postorder(self, root_node):
        # left --> right --> root
        result = []
        if root_node is not None:
            result += self.print_postorder(root_node.left)
            result += self.print_postorder(root_node.right)
            result.append(root_node.value)
        return result

    def get_min(self, node):
        if node is None:
            print('Empty BST')
        else:
            while node.left is not None:
                node = node.left
        print(node.value)

    def get_max(self, node):
        if node is None:
            print('Empty BST')
        else:
            while node.right is not None:
                node = node.right
        print(node.value)

    def search(self, node, value):
        self.root = node
        if node is None:
            print('Empty BST')
        else:
            if node.value > value:
                if node.left is None:
                    print('Value not in BST')
                else:
                    self.search(node.left, value)
            elif node.value < value:
                if node.right is None:
                    print('Value not in BST')
                else:
                    self.search(node.right, value)
            else:
                print(self.print_preorder(node))

    def delete(self, node, value):
        if node is None:
            print('Empty BST')
        else:
            if node.value > value:
                node.left = self.delete(node.left, value)
            elif node.value < value:
                node.right = self.delete(node.right, value)
            else:
                if node.left is None and node.right is None:
                    node = None
                elif node.right is not None:
                    current = node.right
                    while current.left is not None:
                        current = current.left
                    node.value = current.value
                    node.right = self.delete(node.right, node.value)
                else:
                    current = node.left
                    while node.right is not None:
                        node = node.right
                    node.value = current.value
                    node.left = self.delete(node.left, node.value)
        return node


bts = BST()
root = Node(56)
# bts.insert(root, 56)
bts.insert(root, 32)
bts.insert(root, 61)
bts.insert(root, 88)
bts.insert(root, 77)
bts.insert(root, 98)
bts.delete(root, 56)
print(bts.print_inorder(root))
# print(bts.print_preorder(root))
# print(bts.print_postorder(root))
# bts.get_min(root)
# bts.get_max(root)
# bts.search(root, 88)
bts.get_root(root)

