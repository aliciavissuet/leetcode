class myStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def add(self, val):
        self.stack.append(val)

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def sort_stack(self):
        sorted_stack = myStack()
        while len(self.stack > 0):
            temp = self.stack.pop()
            while len(sorted_stack.stack) > 0 and sorted_stack.peek() > temp:
                self.stack.append(sorted_stack.pop())
            sorted_stack.add(temp)
        self.stack = sorted_stack
