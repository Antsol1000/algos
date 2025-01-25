from structures.graph import Graph, DiGraph


def bfs(graph: Graph, start):
    bfs_tree = {start: (None, 0)}

    q = [start]
    while q:
        n = q.pop(0)
        for dst, _ in graph[n]:
            if dst not in bfs_tree:
                bfs_tree[dst] = (n, bfs_tree[n][1] + 1)
                q.append(dst)
    return bfs_tree


def dfs(graph: Graph, start):
    processing_times, time = {}, 1
    _dfs(graph, start, processing_times, time)
    return processing_times


def _dfs(graph: Graph, n, processing_times, time):
    processing_times[n] = [time, None]
    time += 1
    for dst, _ in graph[n]:
        if dst not in processing_times:
            time = _dfs(graph, dst, processing_times, time)
    processing_times[n][1] = time
    time += 1
    return time


def topological_sort(graph: Graph):
    processing_times, time = {}, 0
    for start in graph:
        if start not in processing_times:
            time = _dfs(graph, start, processing_times, time)
    return sorted(processing_times, key=lambda x: processing_times[x][1], reverse=True)


def strongly_connected_components(graph: Graph):
    scc = []
    sorted_nodes = topological_sort(graph)
    transposed_graph = graph.transpose()

    visited = set()
    for n in sorted_nodes:
        if n not in visited:
            scc.append([])

            stack = [n]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    scc[-1].append(node)
                    for ed in transposed_graph[node]:
                        stack.append(ed.dst)

    return scc


if __name__ == '__main__':
    g = DiGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("B", "E")
    g.add_edge("B", "F")
    g.add_edge("C", "D")
    g.add_edge("C", "G")
    g.add_edge("D", "C")
    g.add_edge("D", "H")
    g.add_edge("E", "A")
    g.add_edge("E", "F")
    g.add_edge("F", "G")
    g.add_edge("G", "F")
    g.add_edge("H", "H")
    print(g)
    print("-" * 80)
    print(bfs(g, "A"))
    print("-" * 80)
    print(dfs(g, "A"))
    print("-" * 80)
    print(topological_sort(g))
    print("-" * 80)
    print(strongly_connected_components(g))
    print("-" * 80)
    print(g.transpose())
    print("-" * 80)
