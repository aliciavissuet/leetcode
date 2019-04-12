class tree_node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
#


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


class linked_node:
    def __init__(self, val):
        self.val = val
        self.next = None


def list_of_depths(tree_node):
    list_of_linked_lists = []
    current_q = [tree_node]
    next_q = []
    curr_linked_list_head = None
    curr_linked_node = None
    while len(current_q) > 0 or len(next_q) > 0:
        if len(current_q) == 0:
            list_of_linked_lists.append(curr_linked_list_head)
            current_q = next_q
            next_q = []
            curr_linked_list_head = None
        curr_node = current_q.pop(0)
        if curr_linked_list_head == None:
            curr_linked_list_head = linked_node(curr_node.val)
            curr_linked_node = curr_linked_list_head
        else:
            new_node = linked_node(curr_node.val)
            curr_linked_node.next = new_node
        if tree_node.left:
            next_q.append(tree_node.left)
        if tree_node.right:
            next_q.append(tree_node.right)
    return list_of_linked_lists


a = [1, 2, 3, 4, 5]
tree = minimal_tree(a)


lists = list_of_depths(tree)
print(lists)
