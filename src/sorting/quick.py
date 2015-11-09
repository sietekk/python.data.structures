def quick_sort(alist):
    """ Quick Sort implemented in Python
        Page 225, Listing 5.15
        Complexity: O(n log n), but may degrade to O(n^2) if splitpoints
            not near middle of the list; doesn't require extra space
    """

    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    """ Quick Sort helper function
    """

    if first < last:
        splitpoint = partition(alost, first, last)
        quick_sort_helper(alist, first, splitpoint-1)
        quick_sort_helper(alist, splitpoint+1, last)


def partition(alist, first, last):
    """ Quick Sort helper function
    """

    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmart = leftmark + 1

        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
