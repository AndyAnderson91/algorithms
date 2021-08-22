from algorithms.queue_data_structure import Queue


def breadth_first_search(graph, start, finish=None):
    """
    Breadth-first search algorithm.
    graph: adjacency list representing a graph.
    start: number of starting vertex. (Expects all vertices to be integer numbers from zero)
    finish: number of finishing vertex.
    If 'finish' is not provided, complete traversal of the graph will be done,
    'paths' dictionary will be returned. It will contain shortest path from starting vertex
    to every other vertex of the graph.
    If 'finish' is set, shortest path from starting vertex to finishing one will be returned.
    """
    paths = {key: [start] for key in range(len(graph))}

    # q - queue of vertices to process.
    # visited - list of already processed vertices.
    q, visited = Queue([start]), [start]

    while q:
        # First vertex in a queue - is one to process.
        vertex = q.dequeue()

        # If finish is reached, stops traversal and returns shortest path to it.
        if vertex == finish:
            return paths[finish]

        # Adds neighbors of the current vertex to queue and visited list, if they're not visited yet.
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                q.enqueue(neighbor)
                visited.append(neighbor)

                # Path to neighbor = path to it's parent (vertex) + neighbor.
                paths[neighbor] = paths[vertex] + [neighbor]

    # We're here means finish was not provided or not reached.
    # In first case returns shortest paths from starting vertex to all other vertices.
    # In second case returns appropriate message.
    return paths if finish is None else 'No path from {0} to {1}'.format(start, finish)
