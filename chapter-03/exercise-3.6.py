"""
3.6 Animal Shelter

An animal shelter, which holds only dogs and cats, operators on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based
on arrival time) of all animals at the shelter, or they can select whether
they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create
the data structures to maintain this system and implement operations such as
enqueue, dequeue_any, dequeue_dog and dequeue_cat.
"""

from collections import deque

class Dog:
    def __init__(self,n):
        self.order = -1
        self.name = n

    def set_order(self,ord):
        self.order = ord

    def get_order(self):
        return self.order

    def is_older_than(self,a):
        return self.order < a.get_order()

class Cat:
    def __init__(self, n):
        self.order = -1
        self.name = n

    def set_order(self, ord):
        self.order = ord

    def get_order(self):
        return self.order

    def is_older_than(self, a):
        return self.order < a.get_order()

class AnimalQueue:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enque(self, a):
        a.set_order(self.order)
        self.order += 1

        if type(a) == Dog:
            self.dogs.append(a)
        elif type(a) == Cat:
            self.cats.append(a)

    def dequeue_any(self):
        if len(self.dogs) == 0:
            return self.dequeue_cats()
        elif len(self.cats) == 0:
            return self.dequeue_dogs()

        dog = self.dogs[0]
        cat = self.cats[0]

        if dog.is_older_than(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()

    def dequeue_dogs(self):
        return self.dogs.popleft()

    def dequeue_cats(self):
        return self.cats.popleft()
