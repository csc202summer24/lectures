import dictionary as dct
import priority_queue as pqueue


class WeightedGraph:
    """ A collection of vertices and weighted edges """

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


def add_edge(graph, vertex_u, vertex_v, weight):
    # Get the (inner) dictionary corresponding to the given vertex_u
    #  within the (outer) dictionary.
    # Map the given vertex_v to weight within vertex_u's (inner) dictionary.
    # Get the (inner) dictionary corresponding to the given vertex_v
    #  within the (outer) dictionary.
    # Map the given vertex_u to weight within vertex_v's (inner) dictionary.
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
    # NOTE: In a weighted graph, vertices encountered earlier need not be
    #       closer; we must prioritize by distance rather than time.
    #
    # Create a new, empty priority queue (of vertices to be explored).
    # Enqueue (0, vertex_u) to the priority queue.
    # Create a new, empty dictionary (mapping vertices to distances).
    # Insert vertex_u into the distances dictionary, mapped to 0.
    # Create a new, empty dictionary (mapping vertices to predecessors).
    # Insert vertex_u into the predecessors dictionary, mapped to itself.
    #
    # While the priority queue is not empty, do:
    #     Dequeue a (-1 * priority, current vertex) from the priority queue.
    #     Get the current vertex's distance from the distances dictionary.
    #
    #     If the current vertex is vertex_v, then:
    #         (the shortest path is in the predecessors dictionary)
    #     Else if the current priority is greater than the current vertex's
    #      distance, then:
    #         (we already have a better path)
    #
    #     Get the (inner) dictionary corresponding to the current vertex
    #      within the (outer) dictionary.
    #     Get the list of keys for that (inner) dictionary.
    #     For i from 0 to size - 1 (of that list), do:
    #         Get the i'th key from that list.
    #         Get the i'th key's value from the current vertex's dictionary.
    #         Get the i'th key's distance from the distances dictionary.
    #         Set temp to the current vertex's distance plus the i'th value.
    #
    #         If the i'th key is not in the predecessors dictionary or the
    #          i'th key's distance is less than temp, then:
    #             Insert the i'th key into the predecessors dictionary, mapped
    #              to the current vertex.
    #             Insert the i'th key into the distances dictionary, mapped
    #              to temp.
    #             Enqueue the (-1 * temp, i'th key) to the priority queue.
    #
    # (a path does not exist)
    pass
