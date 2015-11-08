class Queue(object):
    """ Queue implementation in Python
        Page 109, Listing 3.9
        Enqueue is O(n), b/c of insert()
        Dequeue is O(1), b/c of pop()
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
