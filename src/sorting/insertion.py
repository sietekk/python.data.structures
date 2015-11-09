def insertion_sort(alist):
    """ Insertion Sort implemented in Python
        Page 215, Listing 5.12
        Complexity: O(n)
    """

    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue
