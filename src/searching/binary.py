def binary_search(alist, item):
    """ Binary search of ordered list
        Page 192, Figure 5.3
        Complexity: O(log n)
    """

    first = 0
    last = len(alist - 1)
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binary_search_recursive(alist, item):
    """ Recursive binary search of an ordered list
        Page 193, Listing 5.4
        Complexity: Not quite O(log n), b/c Python slice() is O(k)
    """

    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint+1:], item)
