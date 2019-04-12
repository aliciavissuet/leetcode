class tree_node:
    def __init__(self, val):
        self.val = val
        self.status = 'not_visited'
        self.children = []

def route_between_nodes(start_node, end_node):

    to_visit_q = [start_node]

    while (len(to_visit_q) > 0):
        curr = to_visit_q.pop(0)
        curr.status = 'visited'
        if curr.val == end_node.val:
            return True
        for node in curr.children:
            if node.status == 'not_visited':
                node.status = 'visiting'
                to_visit_q.append(node)
    return False
