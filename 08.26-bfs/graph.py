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
    # NOTE: Like a level-order traversal, we must keep track of the vertices to
    #       be explored in such a way that vertices encountered earlier are
    #       explored earlier: shorter paths are tried before longer paths.
    #
    # Create a new, empty queue (of vertices to be explored).
    # Enqueue vertex_u to the queue.
    #
    # NOTE: Unlike a tree traversal, in a graph, any vertex can be connected to
    #       any other vertex; we must keep track of which vertices we've
    #       already explored before and how we got there.
    #
    # Create a new, empty dictionary (mapping vertices to predecessors).
    # Insert vertex_u into the predecessors dictionary, mapped to itself.
    #
    # While the queue is not empty, do:
    #     Dequeue a current vertex from the queue.
    #     If the current vertex is vertex_v, then:
    #         (the shortest path is in the predecessors dictionary)
    #
    #     Get the (inner) dictionary corresponding to the current vertex
    #      within the (outer) dictionary.
    #     Get the list of keys for that (inner) dictionary.
    #     For i from 0 to size - 1 (of that list), do:
    #         Get the i'th key from that list.
    #         If the i'th key is not in the predecessors dictionary, then:
    #             Insert the i'th key into the predecessors dictionary, mapped
    #              to the current vertex.
    #             Enqueue the i'th key to the queue.
    #
    # NOTE: In order to break out of the loop, there must be no more vertices
    #       that we can explore -- any remaining unexplored vertices are
    #       unreachable (no path exists leading to them).
    #
    # (a path does not exist)
    pass
