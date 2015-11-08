from node import Node
from unordered_list import UnorderedList


class OrderedList(UnorderedList):
    """ Ordered List implementation in Python
        Pages 128-136, Listings 3.17-3.22
        Subclassed UnorderedList, search() and add() modified
        Complexity:
            - is_empty O(1)
            - length O(n)
            - Add an item O(1)
            - add O(n)
            - search O(n)
            - remove O(n)
    """

    def __init__(self):
        super(OrderedList, self).__init__()

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def index(self):
        # TODO: Implement
        pass

    def pop(self):
        # TODO: Implement
        pass
