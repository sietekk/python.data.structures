class Deque(object):
    """ Deque implementation in Python
        Page 121, Listing 3.14
        Adding/removing front is O(1)
        Adding/removing rear is O(n)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self, item):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
