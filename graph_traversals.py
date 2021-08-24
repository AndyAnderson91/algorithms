from algorithms.queue_data_structure import Queue
from algorithms.stack_data_structure import Stack


def breadth_first_search(adj_list, start, finish=None):
    """
    Iterative version of BFS implemented via queue.
    :param adj_list: graph as adjacency list.
    :param start: starting vertex.
    :param finish: finishing vertex (optional).
    :return: if finish is not provided, complete traversal of the graph will be done,
    dictionary with shortest paths from starting vertex to all others will be returned.
    if finish is provided, shortest path from starting vertex to finishing vertex will be returned.
    """
    # dictionary with shortest paths from starting vertex to all others.
    paths = {vertex: [start] for vertex in range(len(adj_list))}

    # unvisited - queue of vertices waiting for processing.
    # visited - set of vertices already being processed.
    unvisited, visited = Queue([start]), set()

    while unvisited:
        vertex = unvisited.dequeue()
        # if vertex is not processed yet - process it.
        if vertex not in visited:
            # process(vertex) by appropriate function here.
            # then adds it to the 'visited' list.
            visited.add(vertex)

            # If finish is reached, stops traversal and returns shortest path to it.
            if vertex == finish:
                return paths[finish]

            for neighbor in adj_list[vertex]:
                # if neighbor is not processed yet and not in queue for processing, adds it to the queue.
                if neighbor not in visited and neighbor not in unvisited:
                    unvisited.enqueue(neighbor)

                    # Updates paths.
                    paths[neighbor] = paths[vertex] + [neighbor]

    # We're here means finish was not provided or not reached.
    # In first case returns shortest paths from starting vertex to all other vertices.
    # In second case returns appropriate message.
    return paths if finish is None else 'No path from {0} to {1}'.format(start, finish)


def depth_first_search(adj_list, start):
    """
    Iterative version of DFS implemented via stack.
    :param adj_list: graph as adjacency list.
    :param start: starting vertex.
    :return: list of visited (processed) vertices.
    """
    # unvisited - stack of vertices waiting for processing.
    # visited - set of vertices already being processed.
    unvisited, visited = Stack([start]), set()

    while unvisited:
        vertex = unvisited.pop()
        # if vertex is not processed yet - process it.
        if vertex not in visited:
            # process(vertex) by appropriate function here.
            # then adds it to the 'visited' list.
            visited.add(vertex)

            for neighbor in adj_list[vertex]:
                # if neighbor is not processed yet, adds it to the stack.
                if neighbor not in visited:
                    unvisited.push(neighbor)

    # main purpose of DSF is to process every vertex instead of returning 'visited' list,
    # but it's returned to ensure every vertex in connected graph is visited.
    return visited
