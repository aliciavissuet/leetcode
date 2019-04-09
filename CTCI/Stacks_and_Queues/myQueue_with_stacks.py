class MyQueue:
    def __init__(self):
        self.newest = []
        self.oldest = []

    def size(self):
        return len(self.newest) + len(self.oldest)

    def enqueue(self, val):
        self.newest.append(val)

    def shift_stacks(self):
        if len(self.oldest) == 0:
            while len(self.newest) > 0:
                self.oldest.append(self.newest.pop())

    def dequeue(self):
        self.shift_stacks()
        return self.oldest.pop()

    def peek(self):
        self.shift_stacks()
        return self.oldest[-1]
