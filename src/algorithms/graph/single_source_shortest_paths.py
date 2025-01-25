from structures.graph import Graph
from structures.priorityqueue import BinaryHeap


def bellman_ford(graph: Graph, source):
    distance, predecessor = {n: float('inf') for n in graph}, {n: None for n in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    return distance, predecessor


def dijkstra(graph: Graph, source):
    distance, predecessor = {n: float('inf') for n in graph}, {n: None for n in graph}
    distance[source] = 0

    pq = BinaryHeap()
    for ed in graph[source]:
        pq.push((ed.val, source, ed.dst))

    while not pq.is_empty():
        val, src, dst = pq.pop()
        if distance[dst] > val:
            distance[dst] = val
            predecessor[dst] = src
            for d, v in graph[dst]:
                pq.push((v + val, dst, d))

    return distance, predecessor


def path_from_predecessors(predecessors, target):
    path = []
    while target:
        path.append(target)
        target = predecessors[target]
    return path[::-1]


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
    print("Bellman-Ford algorithm:")
    d, p = bellman_ford(g, 1)
    print(f"Cost from 1 to 5: {d[5]}")
    print(f"Path from 1 to 5: {path_from_predecessors(p, 5)}")
    print("-" * 80)
    print("Dijkstra's algorithm:")
    d, p = dijkstra(g, 1)
    print(f"Cost from 1 to 5: {d[5]}")
    print(f"Path from 1 to 5: {path_from_predecessors(p, 5)}")
    print("-" * 80)
