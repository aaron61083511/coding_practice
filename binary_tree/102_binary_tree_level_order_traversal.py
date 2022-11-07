def levelOrder_iterative(root):
    result = []
    if root is None:
        return result

    level = 0
    queue = [root]
    while queue:
        result.append([])
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            result[level].append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        level += 1
    return result


def levelOrder_recursive(root):
    result = []
    if root is None:
        return result

    def order(node, level):
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        if node.left is not None:
            order(node.left, level + 1)
        if node.righ is not None:
            order(node.right, level + 1)

    order(root, 0)
    return result
