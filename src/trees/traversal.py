def preorder_print(tree):
    """ Preorder Traversal print implemented in Python
        Page 253, Listing 6.11
    """

    if tree:
        print tree.get_root_value()
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder_print(tree):
    """ Postorder Traversal print implemented in Python
        Page 254, Listing 6.13
    """

    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print tree.get_root_value()


def inorder_print(tree):
    """ Inorder Traversal print implemented in Python
        Page 255, Listing 6.15
    """

    if tree != None:
        inorder(tree.get_left_child())
        print tree.get_root_value()
        inorder(tree.get_right_child())
