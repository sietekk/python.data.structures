from node import Node


class UnorderedList(object):
    """ Unordered List implementation in Python
        Pages 128-136, Listings 3.17-3.22
        Complexity: O(n)
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self):
        # TODO: Implement
        pass

    def insert(self):
        # TODO: Implement
        pass

    def index(self):
        # TODO: Implement
        pass

    def pop(self):
        # TODO: Implement
        pass
