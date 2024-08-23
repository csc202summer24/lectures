import dictionary as dct


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()
        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    # Create a new empty dictionary.
    # Map the given vertex to the new (inner) dictionary
    #  within the (outer) dictionary.
    pass


def add_edge(graph, vertex_u, vertex_v):
    # Get the (inner) dictionary corresponding to the given vertex_u
    #  within the (outer) dictionary.
    # Map the given vertex_v to 1 within vertex_u's (inner) dictionary.
    # Get the (inner) dictionary corresponding to the given vertex_v
    #  within the (outer) dictionary.
    # Map the given vertex_u to 1 within vertex_v's (inner) dictionary.
    # Increment the size.
    pass


def remove_vertex(graph, vertex):
    # NOTE: When adding a vertex, we know the vertex has no neighbors. When
    #       removing a vertex, we cannot assume it doesn't have neighbors.
    #
    # Get the (inner) dictionary corresponding to the given vertex
    #  within the (outer) dictionary.
    # Get the list of keys for that (inner) dictionary.
    # For i from 0 to size - 1 (of that list), do:
    #     Get the i'th key from that list.
    #     Remove the edge connecting the given vertex to that i'th key.
    #
    # Remove the given vertex from the (outer) dictionary.
    pass


def remove_edge(graph, vertex_u, vertex_v):
    # Get the (inner) dictionary corresponding to the given vertex_u
    #  within the (outer) dictionary.
    # Remove vertex_v from vertex_u's (inner) dictionary.
    # Get the (inner) dictionary corresponding to the given vertex_v
    #  within the (outer) dictionary.
    # Remove vertex_u from vertex_v's (inner) dictionary.
    # Decrement the size.
    pass


def path(graph, vertex_u, vertex_v):
    pass
