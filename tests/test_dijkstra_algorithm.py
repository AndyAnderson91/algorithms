import pytest
from algorithms.dijkstra_algorithm import dijkstra


con_graph1 = [
    [0, 4],
    [4, 0]
]
con_graph2 = [
    [0, 1, 5],
    [1, 0, 3],
    [5, 3, 0]
]
con_graph3 = [
    [0, 6, 2, 0],
    [0, 0, 0, 1],
    [2, 3, 0, 5],
    [0, 1, 5, 0]
]
discon_graph1 = [
    [0, 0],
    [0, 0]
]
discon_graph2 = [
    [0, 0, 5],
    [0, 0, 0],
    [0, 0, 0]
]
inf = float('inf')


@pytest.mark.parametrize('graph, start, paths, paths_weights', [
    (con_graph1, 0, [(0, ), (0, 1)], [0, 4]),
    (con_graph1, 1, [(1, 0), (1, )], [4, 0]),
    (con_graph2, 0, [(0, ), (0, 1), (0, 1, 2)], [0, 1, 4]),
    (con_graph2, 1, [(1, 0), (1, ), (1, 2)], [1, 0, 3]),
    (con_graph2, 2, [(2, 1, 0), (2, 1), (2, )], [4, 3, 0]),
    (con_graph3, 0, [(0, ), (0, 2, 1), (0, 2), (0, 2, 1, 3)], [0, 5, 2, 6]),
    (con_graph3, 1, [(1, 3, 2, 0), (1, ), (1, 3, 2), (1, 3)], [8, 0, 6, 1]),
    (con_graph3, 2, [(2, 0), (2, 1), (2, ), (2, 1, 3)], [2, 3, 0, 4]),
    (con_graph3, 3, [(3, 2, 0), (3, 1), (3, 2), (3, )], [7, 1, 5, 0]),
    (discon_graph1, 0, [(0, ), (0, )], [0, inf]),
    (discon_graph1, 1, [(1, ), (1, )], [inf, 0]),
    (discon_graph2, 0, [(0,), (0, ), (0, 2)], [0, inf, 5]),
    (discon_graph2, 1, [(1, ), (1, ), (1, )], [inf, 0, inf]),
    (discon_graph2, 2, [(2, ), (2, ), (2, )], [inf, inf, 0]),
])
def test_graph_full_traversal(graph, start, paths, paths_weights):
    assert dijkstra(graph, start) == (paths, paths_weights)


@pytest.mark.parametrize('graph, start, finish, path, path_weight', [
    (con_graph1, 1, 0, (1, 0), 4),
    (con_graph2, 0, 2, (0, 1, 2), 4),
    (con_graph3, 3, 0, (3, 2, 0), 7),
    (discon_graph1, 0, 1, (0, ), inf),
    (discon_graph2, 0, 2, (0, 2), 5),
])
def test_find_shortest_path_to_finish_and_its_weight(graph, start, finish, path, path_weight):
    assert dijkstra(graph, start, finish) == (path, path_weight)
