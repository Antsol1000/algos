from copy import copy

from algorithms.graph.single_source_shortest_paths import bellman_ford, dijkstra
from structures.graph import Graph


def floyd_warshall(graph: Graph):
    distance = {n: {m: float('inf') for m in graph} for n in graph}
    for n in graph:
        distance[n][n] = 0
        for m, w in graph[n]:
            distance[n][m] = w

    for _ in range(len(graph)):
        for u in graph:
            for v in graph:
                for w in graph:
                    if distance[u][v] > distance[u][w] + distance[w][v]:
                        distance[u][v] = distance[u][w] + distance[w][v]

    return distance


def johnson(graph: Graph):
    distances = {}
    _g = copy(graph)

    _g.add_node('__q')
    for v in graph:
        _g.add_edge('__q', v, 0)
    h, _ = bellman_ford(_g, '__q')
    _g.remove_node('__q')

    for u in _g:
        for ed in _g[u]:
            ed.val = ed.val + h[u] - h[ed.dst]

    for u in _g:
        distances[u], _ = dijkstra(_g, u)
        for v in distances[u]:
            if distances[u][v] < float('inf'):
                distances[u][v] = distances[u][v] + h[v] - h[u]

    return distances


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 6, 9)
    print(g)
    print("-" * 80)
    print("Floyd-Warshall algorithm:")
    d = floyd_warshall(g)
    for dd in d.values():
        print(list(dd.values()))
    print("-" * 80)
    print("Johnson's algorithm:")
    d = johnson(g)
    for dd in d.values():
        print(list(dd.values()))
    print("-" * 80)
