"""
Tests on BFS and DFS algorithms.
Graphs are represented as adjacency lists.
"""
import pytest
from algorithms.graph_traversals import breadth_first_search, depth_first_search


# Connected graphs.
GRAPH1 = [[1], [0]]
GRAPH2 = [[1, 2], [2], [0, 1]]
GRAPH3 = [[1, 2], [0, 4], [0, 3, 4], [2, 4], [1, 2, 3]]

# Disconnected graphs.
GRAPH4 = [[1], [0], []]
GRAPH5 = [[1, 2], [2], [0], [4], []]


@pytest.mark.parametrize('adj_list, start, paths', [
    (GRAPH1, 0, {0: [0], 1: [0, 1]}),
    (GRAPH1, 1, {0: [1, 0], 1: [1]}),
    (GRAPH2, 0, {0: [0], 1: [0, 1], 2: [0, 2]}),
    (GRAPH2, 1, {0: [1, 2, 0], 1: [1], 2: [1, 2]}),
    (GRAPH2, 2, {0: [2, 0], 1: [2, 1], 2: [2]}),
    (GRAPH3, 0, {0: [0], 1: [0, 1], 2: [0, 2], 3: [0, 2, 3], 4: [0, 1, 4]}),
    (GRAPH3, 1, {0: [1, 0], 1: [1], 2: [1, 0, 2], 3: [1, 4, 3], 4: [1, 4]}),
    (GRAPH3, 2, {0: [2, 0], 1: [2, 0, 1], 2: [2], 3: [2, 3], 4: [2, 4]}),
    (GRAPH3, 3, {0: [3, 2, 0], 1: [3, 4, 1], 2: [3, 2], 3: [3], 4: [3, 4]}),
    (GRAPH3, 4, {0: [4, 1, 0], 1: [4, 1], 2: [4, 2], 3: [4, 3], 4: [4]}),
    (GRAPH4, 0, {0: [0], 1: [0, 1], 2: [0]}),
    (GRAPH4, 1, {0: [1, 0], 1: [1], 2: [1]}),
    (GRAPH4, 2, {0: [2], 1: [2], 2: [2]}),
    (GRAPH5, 0, {0: [0], 1: [0, 1], 2: [0, 2], 3: [0], 4: [0]}),
    (GRAPH5, 1, {0: [1, 2, 0], 1: [1], 2: [1, 2], 3: [1], 4: [1]}),
    (GRAPH5, 2, {0: [2, 0], 1: [2, 0, 1], 2: [2], 3: [2], 4: [2]}),
    (GRAPH5, 3, {0: [3], 1: [3], 2: [3], 3: [3], 4: [3, 4]}),
    (GRAPH5, 4, {0: [4], 1: [4], 2: [4], 3: [4], 4: [4]})
])
def test_bfs_full_traversal(adj_list, start, paths):
    assert breadth_first_search(adj_list, start) == paths


@pytest.mark.parametrize('adj_list, start, finish, path', [
    (GRAPH1, 0, 1, [0, 1]),
    (GRAPH2, 1, 0, [1, 2, 0]),
    (GRAPH3, 3, 1, [3, 4, 1]),
    (GRAPH4, 1, 0, [1, 0]),
    (GRAPH5, 3, 4, [3, 4])
])
def test_bfs_shortest_existent_path_from_start_to_finish(adj_list, start, finish, path):
    assert breadth_first_search(adj_list, start, finish) == path


@pytest.mark.parametrize('adj_list, start, finish', [
    (GRAPH4, 0, 2),
    (GRAPH4, 1, 2),
    (GRAPH4, 2, 0),
    (GRAPH4, 2, 1),
    (GRAPH5, 0, 3),
    (GRAPH5, 0, 4),
    (GRAPH5, 1, 3),
    (GRAPH5, 1, 4),
    (GRAPH5, 2, 3),
    (GRAPH5, 2, 4),
    (GRAPH5, 3, 0),
    (GRAPH5, 3, 1),
    (GRAPH5, 3, 2),
    (GRAPH5, 4, 0),
    (GRAPH5, 4, 1),
    (GRAPH5, 4, 2),
    (GRAPH5, 4, 3)
])
def test_bfs_path_between_start_and_finish_doesnt_exist(adj_list, start, finish):
    assert breadth_first_search(adj_list, start, finish) == 'No path from {0} to {1}'.format(start, finish)


@pytest.mark.parametrize('adj_list, start, visited', [
    (GRAPH1, 0, {0, 1}),
    (GRAPH1, 1, {0, 1}),
    (GRAPH2, 0, {0, 1, 2}),
    (GRAPH2, 1, {0, 1, 2}),
    (GRAPH2, 2, {0, 1, 2}),
    (GRAPH3, 0, {0, 1, 2, 3, 4}),
    (GRAPH3, 1, {0, 1, 2, 3, 4}),
    (GRAPH3, 2, {0, 1, 2, 3, 4}),
    (GRAPH3, 3, {0, 1, 2, 3, 4}),
    (GRAPH3, 4, {0, 1, 2, 3, 4}),
    (GRAPH4, 0, {0, 1}),
    (GRAPH4, 1, {0, 1}),
    (GRAPH4, 2, {2}),
    (GRAPH5, 0, {0, 1, 2}),
    (GRAPH5, 1, {0, 1, 2}),
    (GRAPH5, 2, {0, 1, 2}),
    (GRAPH5, 3, {3, 4}),
    (GRAPH5, 4, {4}),
])
def test_dfs_visit_all_reachable_vertices(adj_list, start, visited):
    assert depth_first_search(adj_list, start) == visited
