"""
Tests on Dijkstra algorithm.
Graphs are represented as adjacency matrices.
"""
import pytest
from dijkstra_algorithm import dijkstra


# Connected graphs.
GRAPH1 = [
    [0, 4],
    [4, 0]
]
GRAPH2 = [
    [0, 1, 5],
    [1, 0, 3],
    [5, 3, 0]
]
GRAPH3 = [
    [0, 6, 2, 0],
    [0, 0, 0, 1],
    [2, 3, 0, 5],
    [0, 1, 5, 0]
]

# Disconnected graphs.
GRAPH4 = [
    [0, 0],
    [0, 0]
]
GRAPH5 = [
    [0, 0, 5],
    [0, 0, 0],
    [0, 0, 0]
]

# Infinity.
inf = float('inf')


@pytest.mark.parametrize('adj_matrix, start, paths, paths_weights', [
    (GRAPH1, 0, [(0, ), (0, 1)], [0, 4]),
    (GRAPH1, 1, [(1, 0), (1, )], [4, 0]),
    (GRAPH2, 0, [(0, ), (0, 1), (0, 1, 2)], [0, 1, 4]),
    (GRAPH2, 1, [(1, 0), (1, ), (1, 2)], [1, 0, 3]),
    (GRAPH2, 2, [(2, 1, 0), (2, 1), (2, )], [4, 3, 0]),
    (GRAPH3, 0, [(0, ), (0, 2, 1), (0, 2), (0, 2, 1, 3)], [0, 5, 2, 6]),
    (GRAPH3, 1, [(1, 3, 2, 0), (1, ), (1, 3, 2), (1, 3)], [8, 0, 6, 1]),
    (GRAPH3, 2, [(2, 0), (2, 1), (2, ), (2, 1, 3)], [2, 3, 0, 4]),
    (GRAPH3, 3, [(3, 2, 0), (3, 1), (3, 2), (3, )], [7, 1, 5, 0]),
    (GRAPH4, 0, [(0, ), (0, )], [0, inf]),
    (GRAPH4, 1, [(1, ), (1, )], [inf, 0]),
    (GRAPH5, 0, [(0,), (0, ), (0, 2)], [0, inf, 5]),
    (GRAPH5, 1, [(1, ), (1, ), (1, )], [inf, 0, inf]),
    (GRAPH5, 2, [(2, ), (2, ), (2, )], [inf, inf, 0]),
])
def test_graph_full_traversal(adj_matrix, start, paths, paths_weights):
    assert dijkstra(adj_matrix, start) == (paths, paths_weights)


@pytest.mark.parametrize('adj_matrix, start, finish, path, path_weight', [
    (GRAPH1, 1, 0, (1, 0), 4),
    (GRAPH2, 0, 2, (0, 1, 2), 4),
    (GRAPH3, 3, 0, (3, 2, 0), 7),
    (GRAPH4, 0, 1, (0, ), inf),
    (GRAPH5, 0, 2, (0, 2), 5),
])
def test_find_shortest_path_to_finish_and_its_weight(adj_matrix, start, finish, path, path_weight):
    assert dijkstra(adj_matrix, start, finish) == (path, path_weight)
