import dictionary as dct


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # NOTE: Generally speaking, a dictionary is both smaller than a
        #       true matrix and faster than a list:
        #         * The matrix below is the "outer dictionary", which maps
        #           vertex identifiers to "inner dictionaries".
        #         * Each "inner dictionary" then corresponds to a single
        #           vertex, and will map adjacent vertices' identifiers to 1.
        #       ...that is, this will be a 2D dictionary of dictionaries.
        #
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()

        # NOTE: The number of vertices is the number of keys in the "outer
        #       dictionary", but there's no easy way to compute the number of
        #       edges unless we already have that number stored.
        #
        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    pass


def add_edge(graph, vertex_u, vertex_v):
    pass


def remove_vertex(graph, vertex):
    pass


def remove_edge(graph, vertex_u, vertex_v):
    pass


def path(graph, vertex_u, vertex_v):
    pass
