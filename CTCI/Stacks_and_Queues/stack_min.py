# stacks and queues
# to access stack min in O(1) save local min in each node of stack


class Node:
    def __init__(self, value, stack_min):
        self.value = value
        self.stack_min = stack_min


class Stack:
    def __init__(self):
        self.arr = []
        self.min = 0

    def push(self, val):

        new_node = Node(val, self.min)
        self.arr.append(new_node)
        if self.min:
            self.min = min(val, self.min)
        else:
            self.min = val

    def pop(self):
        node = self.arr.pop()
        self.min = node.stack_min
        return node.value
