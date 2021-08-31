"""
Dijkstra algorithm implementation.
Accepts graph as adjacency matrix.
"""


def dijkstra(adj_matrix, start, finish=None):
    """
    If finish is not given:
    Returns list with shortest paths to each vertex from starting one and list with their weights.
    Vertices number are indexes in both lists.
    Else:
    Returns shortest path and it's weight from starting vertex to finishing one.

    (!) Uncomment appropriate 'return' lines in code for more convenient string output.
    """
    paths = [(start, )]*len(adj_matrix)
    paths_weights = [float('inf') if i != start else 0 for i in range(len(adj_matrix))]
    unvisited, visited = {start}, set()

    while unvisited:
        parent_vertex = min(unvisited, key=lambda vertex: paths_weights[vertex])
        if parent_vertex == finish:
            "(!) Uncomment next line for more convenient string output."
            # return friendly_output(adj_matrix, start, paths, paths_weights, finish)

            return paths[finish], paths_weights[finish]

        unvisited.remove(parent_vertex)
        visited.add(parent_vertex)

        for child_vertex in range(len(adj_matrix)):
            parent_child_edge_weight = adj_matrix[parent_vertex][child_vertex]
            if child_vertex not in visited and parent_child_edge_weight:
                unvisited.add(child_vertex)
                possible_new_weight = paths_weights[parent_vertex] + parent_child_edge_weight

                if possible_new_weight < paths_weights[child_vertex]:
                    paths_weights[child_vertex] = possible_new_weight
                    paths[child_vertex] = paths[parent_vertex] + (child_vertex, )

    "(!) Uncomment next line for more convenient string output."
    # return friendly_output(adj_matrix, start, paths, paths_weights, finish)

    if finish is not None:
        return paths[finish], paths_weights[finish]
    else:
        return paths, paths_weights


def friendly_output(graph, start_v, paths_array, paths_weights_array, finish_v):
    if start_v == finish_v:
        return 'Starting and finishing vertices are equal.'
    elif finish_v is not None and (finish_v < 0 or finish_v >= len(graph)):
        return 'Finishing vertex is out of graph range.'
    else:
        lines = []
        for vertex in range(len(graph)):
            if vertex != start_v:
                line = 'From {0} to {1} (weight: {3}): {2}'.format(
                    str(start_v),
                    str(vertex),
                    ' --> '.join([str(v) for v in paths_array[vertex]]),
                    str(paths_weights_array[vertex]),
                )
                if vertex == finish_v:
                    return line

                lines.append(line)

        return '\n'.join(lines)
