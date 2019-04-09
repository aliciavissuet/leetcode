class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, val):
        self.arr.append(val)
        return val

    def dequeue(self):
        dequeued = self.arr.pop(0)
        return dequeued

    def peek(self):
        return self.arr[0]

# Animal Shelter


class Animal:
    def __init__(self, name, curr_time):
        self.name = name
        self.time = curr_time


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue_dog(self, dog, curr_time):
        dog = Animal(dog, curr_time)
        self.dogs.enqueue(dog)

    def dequeue_dog(self):
        self.dogs.dequeue()

    def enqueue_cat(self, cat, curr_time):
        cat = Animal(cat, curr_time)
        self.cats.enqueue(cat)

    def dequeue_cat(self):
        self.cats.dequeue()

    def dequeue_any(self):
        cat_time = self.cats.peek().time
        dog_time = self.dogs.peek().time
        if cat_time < dog_time:
            self.dequeue_cat()
        else:
            self.dequeue_dog()
