def selection_sort(alist):
    """ Selection Sort implemented in Python
        Page 211, Listing 5.11
        Complexity: O(n^2)
    """

    for fillslot in range(len(alist)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[fillslot]
        alist[fillslot] = alist[position_of_max]
        alost[position_of_max] = temp
