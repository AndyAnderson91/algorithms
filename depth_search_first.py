from stack_data_structure import Stack


def depth_first_search_iterative(graph, start):
    s, visited = Stack([start]), [start]

    while s:

        vertex = s.pop()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                s.push(neighbor)
                visited.append(neighbor)

    return visited


def depth_first_search_recursive(graph, vertex, visited=None):
    visited = [] if visited is None else visited
    visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            depth_first_search_recursive(graph, neighbor, visited)

    return visited


graph1 = [
    [0, 6, 2, 0],
    [6, 0, 3, 1],
    [2, 3, 0, 5],
    [0, 1, 5, 0]
]
