class Node(object):
    """ Node implementation in Python for Linked Lists
        Page 128, Listing 3.16
        For both unordered and ordered linked lists
    """

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext
