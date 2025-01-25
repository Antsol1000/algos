from structures.disjoint_sets import DisjointSets
from structures.graph import Graph
from structures.priorityqueue import BinaryHeap


def mst_kruskal(graph: Graph):
    edges = []
    dj = DisjointSets(graph.get_node_keys())
    sorted_edges = sorted(graph.get_edges(), key=lambda x: x[2])

    for src, dst, val in sorted_edges:
        if dj.find(src) != dj.find(dst):
            edges.append((src, dst, val))
            dj.union(src, dst)

    return edges


def mst_prim(graph: Graph):
    edges = []

    first_node = next(iter(graph))
    pq = BinaryHeap()
    for ed in graph[first_node]:
        pq.push((ed.val, first_node, ed.dst))
    visited = {first_node}

    while not pq.is_empty():
        val, src, dst = pq.pop()
        if dst not in visited:
            visited.add(dst)
            edges.append((src, dst, val))
            for d, v in graph[dst]:
                if d not in visited:
                    pq.push((v, dst, d))

    return edges


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'H', 8)
    g.add_edge('B', 'C', 8)
    g.add_edge('B', 'H', 11)
    g.add_edge('C', 'D', 7)
    g.add_edge('C', 'F', 4)
    g.add_edge('C', 'I', 2)
    g.add_edge('D', 'E', 9)
    g.add_edge('D', 'F', 14)
    g.add_edge('E', 'F', 10)
    g.add_edge('F', 'G', 2)
    g.add_edge('G', 'H', 1)
    g.add_edge('G', 'I', 6)
    g.add_edge('H', 'I', 7)
    print(g)
    print("-" * 80)
    result_kruskal = mst_kruskal(g)
    print("Kurskal's algorithm:")
    print("Total weight:", sum([x[2] for x in result_kruskal]))
    print("Edges: " + ", ".join([f"{x[0]}-{x[1]}({x[2]})" for x in result_kruskal]))
    print("-" * 80)
    result_prim = mst_prim(g)
    print("Prim's algorithm:")
    print("Total weight:", sum([x[2] for x in result_prim]))
    print("Edges: " + ", ".join([f"{x[0]}-{x[1]}({x[2]})" for x in result_prim]))
    print("-" * 80)
