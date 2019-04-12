class tree_node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minimal_tree(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return tree_node(arr[0])
    mid = arr.pop(len(arr)//2)
    root = tree_node(mid)
    root.left = minimal_tree(arr[0:len(arr)//2])
    root.right = minimal_tree(arr[len(arr)//2:])
    return root


def in_order_print_tree(tree_node):
    if tree_node.left:
        in_order_print_tree(tree_node.left)
    print(tree_node.val)
    if tree_node.right:
        in_order_print_tree(tree_node.right)


a = [1, 2, 3, 4, 5, 6]
in_order_print_tree(minimal_tree(a))
