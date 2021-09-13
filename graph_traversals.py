"""
Breadth-first search and depth-first search algorithms implementations.
Both function accepts graph represented as adjacency list.
"""


from stack_and_queue import Stack, Queue


def breadth_first_search(adj_list, start, finish=None):
    """
    Iterative version implemented via queue.
    If finish is not given:
    Complete full graph traversal. Returns dictionary with (vertex, shortest path to it from start) items.
    Else:
    Stops as soon as the finishing vertex found.
    Returns shortest path from starting vertex to it.
    If no path to finishing vertex, returns appropriate message.
    """
    paths = {vertex: [start] for vertex in range(len(adj_list))}
    unvisited, visited = Queue([start]), set()

    while unvisited:
        vertex = unvisited.dequeue()
        if vertex not in visited:
            # process(vertex) by appropriate function here.
            visited.add(vertex)

            if vertex == finish:
                return paths[finish]

            for neighbor in adj_list[vertex]:
                # if neighbor is not processed yet and not in queue for processing, adds it to the queue,
                # and updates paths.
                if neighbor not in visited and neighbor not in unvisited:
                    unvisited.enqueue(neighbor)
                    paths[neighbor] = paths[vertex] + [neighbor]

    return paths if finish is None else 'No path from {0} to {1}'.format(start, finish)


def depth_first_search(adj_list, start):
    """
    Iterative version implemented via stack.
    Returns list of visited vertices.
    """
    unvisited, visited = Stack([start]), set()

    while unvisited:
        vertex = unvisited.pop()
        if vertex not in visited:
            # process(vertex) by appropriate function here.
            visited.add(vertex)

            for neighbor in adj_list[vertex]:
                # if neighbor is not processed yet, adds it to the stack.
                if neighbor not in visited:
                    unvisited.push(neighbor)

    return visited
