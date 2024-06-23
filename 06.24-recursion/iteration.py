def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: A list of comparable elements
    :return: The largest element, or None if empty
    """
    temp = None

    for element in lst:
        if temp is None or element > temp:
            temp = element

    return temp


print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
