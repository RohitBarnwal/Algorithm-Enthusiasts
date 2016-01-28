class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_value(lst, node):
    if node is None:
        return
    lst.append(node.val)
    get_value(lst, node.left)
    get_value(lst, node.right)


def pre_order_traversal_recursive(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    lst = []
    get_value(lst, root)
    return lst


def pre_order_traversal(root):
    res = []
    if root is None:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def pre_order_traversal2(root):
    res = []
    stack = []
    node = root
    while stack or node is not None:
        if node:
            stack.append(node)
            res.append(node.val)
            node = node.left
        else:
            stack_node = stack.pop()
            node = stack_node.right
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(pre_order_traversal_recursive(root))

    assert pre_order_traversal_recursive(root) == [1, 2, 3, 4, 5, 6, 7]
    assert pre_order_traversal(root) == [1, 2, 3, 4, 5, 6, 7]
    assert pre_order_traversal2(root) == [1, 2, 3, 4, 5, 6, 7]
