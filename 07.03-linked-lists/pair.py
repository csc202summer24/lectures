# Like lists, pairs are ordered collections, but unlike lists, pairs can only
#  contain exactly two elements. If we want to contain, for example, three
#  elements, we could create a "triple", but that would just create the same
#  problem for four elements...

class Pair:
    """ A pair of elements """

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return (type(other) == type(self)
                and other.first == self.first
                and other.second == self.second)

    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.second)

# ...alternatively, since the elements can have any type, the second element
#  could be another pair:

lst = Pair('a', Pair('b', Pair('c', None)))

# That is to say, within each pair, the first element is an actual element of
#  the list, and the second element is the rest of the list.
