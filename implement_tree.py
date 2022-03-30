class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTS(object):
    def __init__(self):
        self.root = None

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


bts = BTS()
root = Node(56)
bts.insert(root, 56)
bts.insert(root, 32)
bts.insert(root, 61)
bts.insert(root, 88)
bts.insert(root, 77)
bts.insert(root, 98)
print(bts.print_inorder(root))
print(bts.print_preorder(root))
print(bts.print_postorder(root))
