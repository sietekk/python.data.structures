class HashTable(object):
    """ Hash function implemented in Python
        Pages 203-205, Listings 5.6-5.8
        Complexity:
            - Theoretical: O(1)
            - Actual:
                - Successful: 1+(lambda/2)
                - Unsuccessful: lambda 
    """

    def __init__(self, init_size):
        self.size = init_size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.__hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            nextslot = self.__rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.__rehash(nextslot, len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data # replace

    def __hashfunction(self, key, size):
        return key % size

    def __rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.__hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position =  self.__rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def del(self):
        # TODO: Implement
        pass

    def len(self):
        # TODO: Implement
        pass

    def __contains__(self):
        # TODO: Implement; implements "in" keyword
        pass
