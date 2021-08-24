from stack_data_structure import Stack


def depth_first_search(adj_list, start):
    """
    Iterative version implemented via stack.
    :param adj_list: graph as adjacency list.
    :param start: starting vertex.
    :return: list of visited (processed) vertices.
    """
    # unvisited - stack with vertices waiting for processing.
    # visited - array with vertices already being processed.
    unvisited, visited = Stack([start]), []

    while unvisited:
        vertex = unvisited.pop()
        # if vertex is not processed yet - process it.
        if vertex not in visited:
            # process(vertex) with using appropriate function here.
            # then adds it to the 'visited' list.
            visited.append(vertex)

            for neighbor in adj_list[vertex]:
                # if neighbor is not processed yet, adds it to the stack.
                if neighbor not in visited:
                    unvisited.push(neighbor)

    # main purpose of DSF is to process every vertex instead of returning 'visited' list,
    # but it's returned to ensure every vertex in connected graph is visited.
    return visited
