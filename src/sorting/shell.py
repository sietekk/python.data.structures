def shell_sort(alist):
    """ Shell Sort implemented in Python
        Page 218, Listing 5.13
        Complexity: between O(n^2) and O(n)
    """

    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)

        print "After increments of size ", sublistcount, \
            ", the list is: ", alist

        sublistcount = sublistcount // 2


def gap_insertion_sort(alist, start, gap):
    """ Helper function for shell_sort()
    """

    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while posotion >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue
