def max_element(lst):
    """
    Find the largest element in a list -- iteration and recursion are two
    different ways of approaching the same problem; this function is still
    trying to solve the same problem as the iterative function.

    :param lst: A list of comparable elements
    :return: The largest element, or None if empty
    """

    # A function ought to solve a problem, so a recursive function ought to
    #  generally solve larger problems by reducing them to smaller problems.

    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        return max(max_element(lst[1:]), lst[0])


print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
