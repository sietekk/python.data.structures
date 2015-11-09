def bubble_sort(alist):
    """ Bubble Sort implemented in Python
        Page 209, Listing 5.9
        Complexity: O(n^2)
    """

    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def short_bubble_sort(alist):
    """ Short Bubble Sort implemented in Python
        Page 211, Listing 5.10
        Complexity: ???
    """

    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i] = temp
        passnume = passnum - 1
