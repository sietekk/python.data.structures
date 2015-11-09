def lists_binary_tree(r):
    """ Binary Tree list of lists implementation in Python
        Pages 239-241, Listings 6.1-6.4
    """

    return [r, [], []]


def insert_left(root, new_branch):
    """ Inserts left child
    """

    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insert_right(root, new_branch):
    """ Inserts right child
    """

    t.root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t]]
    else:
        root.insert(2, [[new_branch, [], []])

    return root


def get_root_value(root):
    """ Gets root value
    """

    return root[0]


def set_root_value(root, new_value):
    """ Sets new root value
    """

    root[0] = new_value


def get_left_child(root):
    """ Get left child
    """

    return root[1]


def get_right_child(root):
    """ Get right child
    """

    return root[2]
