class Pair:
    """ A pair of elements """

    # This creates a new type, "Pair", but because this is a new type, the
    #  Python interpreter has no idea how to operate on it.

    def __init__(self, first, second):

        # This tells the interpreter how to create a value of type "Pair".

        self.first = first
        self.second = second

    def __eq__(self, other):

        # This tells the interpreter when two values of type "Pair" are equal.

        return (type(other) == type(self)
                and other.first == self.first
                and other.second == self.second)

    def __repr__(self):

        # This tells the interpreter how to print out a value of type "Pair".

        return "Pair(%r, %r)" % (self.first, self.second)


def swap(pair):
    """
    Swap the elements of a pair.

    :param pair: A pair of elements
    :return: A new pair with swapped elements.
    """
    return Pair(pair.second, pair.first)
