def unordered_sequential_search(alist, item):
    """ Sequential Search of unordered list
        Page 189, Listing 5.1
        Complexity: O(n)
    """

    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(alist, item):
    """ Sequential search of ordered list
        Page 191, Listing 5.2
        Complexity: O(n)
    """

    post = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = post + 1

    return found
