def dijkstra(adj_matrix, start, finish=None):
    """
    Dijkstra's algorithm implementation.
    :param adj_matrix: graph as adjacency matrix.
    :param start: starting vertex.
    :param finish: finishing vertex.
    :return: paths and weights from starting vertex to all other vertices if 'finish' is not provided,
    and path and weight to finishing vertex if it's provided.
    Uncomment appropriate 'return' lines in code for more convenient string output.
    """
    # array with paths from starting vertex to others.
    paths = [(start, )]*len(adj_matrix)
    # array with paths weights from starting vertex to others.
    paths_weights = [float('inf') if i != start else 0 for i in range(len(adj_matrix))]
    # unvisited - array with vertices waiting for processing, visited - array with vertices already being processed.
    unvisited, visited = {start}, set()

    while unvisited:
        # At each iteration looks from parent vertex to it's child vertices and update their weights (if needed).
        # parent_vertex - is one with the minimum weight from all vertices in 'unvisited' array.
        parent_vertex = min(unvisited, key=lambda v_num: paths_weights[v_num])
        # Currently processed vertex's weight won't become less,
        # so if 'finish' argument matches parent_vertex, no point to search for something else.
        if parent_vertex == finish:
            "Uncomment next line for more convenient string output."
            # return friendly_output(adj_matrix, start, paths, paths_weights, finish)

            return paths[finish], paths_weights[finish]

        unvisited.remove(parent_vertex)
        visited.add(parent_vertex)

        for child_vertex in range(len(adj_matrix)):
            # finds child vertices that are not visited yet.
            parent_child_edge_weight = adj_matrix[parent_vertex][child_vertex]
            if child_vertex not in visited and parent_child_edge_weight:
                unvisited.add(child_vertex)
                # weight of a child vertex, calculated as parent weight + weight of the edge between parent and child.
                possible_new_weight = paths_weights[parent_vertex] + parent_child_edge_weight
                # updates child's weight if it's potential weight is lower than actual.
                if possible_new_weight < paths_weights[child_vertex]:
                    paths_weights[child_vertex] = possible_new_weight
                    paths[child_vertex] = paths[parent_vertex] + (child_vertex, )

    "Uncomment next line for more convenient string output."
    # return friendly_output(adj_matrix, start, paths, paths_weights, finish)

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
