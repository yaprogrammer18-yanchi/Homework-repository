from src.Depth_first_search.depth_first_search_class import Graph

def test_linear_graph():
    """ 1 - 2 - 3 """
    graph = Graph([1, 2, 3], [(1, 2), (2, 3)])
    dfs_result = graph.dfs()
    assert len(dfs_result) == 3
    assert set(dfs_result) == {1, 2, 3}
    iter_result = list(graph)
    assert iter_result == dfs_result


def test_branched_graph():
    """    1
         /  \
        2    3
        |
        4
    """
    graph = Graph([1, 2, 3, 4], [(1, 2), (1, 3), (2, 4)])
    dfs_result = graph.dfs()
    assert len(dfs_result) == 4
    assert set(dfs_result) == {1, 2, 3, 4}
    assert dfs_result[0] == 1

def test_disconnected_graph():
    """ 1-2   3-4 """
    graph = Graph([1, 2, 3, 4], [(1, 2), (3, 4)])
    dfs_result = graph.dfs()
    assert len(dfs_result) == 4
    assert set(dfs_result) == {1, 2, 3, 4}


def test_single_vertex():
    graph = Graph([1], [])
    dfs_result = graph.dfs()
    assert dfs_result == [1]
    assert list(graph) == [1]

def test_empty_graph():
    graph = Graph([], [])
    dfs_result = graph.dfs()
    assert dfs_result == []
    assert list(graph) == []


def test_multiple_iterations():
    graph = Graph([1, 2], [(1, 2)])
    first_iter = list(graph)
    second_iter = list(graph)
    assert first_iter == second_iter
    assert len(first_iter) == 2


def test_dfs_order():
    graph = Graph([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (1, 4)])
    dfs_result = graph.dfs()
    assert len(dfs_result) == 4
    assert dfs_result[0] == 1
    assert dfs_result == [1, 2, 3, 4]



def test_complex_graph():
    graph = Graph([1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])
    dfs_result = graph.dfs()
    assert len(dfs_result) == 5
    assert set(dfs_result) == {1, 2, 3, 4, 5}
    assert dfs_result[0] == 1


