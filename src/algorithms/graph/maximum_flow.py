from structures.graph import Graph, DiGraph


def edmonds_karp(graph: Graph, source, sink) -> int:
    def bfs(graph, source, sink, parent):
        visited = {key: False for key in graph.nodes.keys()}
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for edge in graph.nodes[u].neighbors:
                v = edge.dst
                if not visited[v] and residual_graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        return visited[sink]

    max_flow = 0
    parent = {key: -1 for key in graph.nodes.keys()}
    residual_graph = {u: {v: 0 for v in graph.nodes.keys()} for u in graph.nodes.keys()}

    for u in graph:
        for edge in graph[u]:
            v = edge.dst
            residual_graph[u][v] = edge.val

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow


def push_relabel(graph: Graph, source, sink) -> int:
    n = len(graph.nodes)
    flow, capacity, height, excess = {}, {}, {}, {}

    for node in graph:
        flow[node] = {i: 0 for i in graph}
        capacity[node] = {i: 0 for i in graph}
        excess[node] = 0
        height[node] = 0

    for node in graph:
        for edge in graph[node]:
            capacity[node][edge.dst] = edge.val

    def push(src, dst):
        amt = min(excess[src], capacity[src][dst] - flow[src][dst])
        flow[src][dst] += amt
        flow[dst][src] -= amt
        excess[src] -= amt
        excess[dst] += amt

    def relabel(src):
        height[src] = 1 + min(height[i] for i in graph if capacity[src][i] - flow[src][i] > 0)

    height[source] = n
    excess[source] = float('inf')
    for i in graph:
        push(source, i)

    seen = {i: 0 for i in graph}
    nodes = [i for i in graph if i not in (source, sink)]
    p = 0
    while p < len(nodes):
        node = nodes[p]
        old_height = height[node]
        while excess[node] > 0:
            if seen[node] < n:
                dst = seen[node]
                if capacity[node][dst] - flow[node][dst] > 0 and height[node] > height[dst]:
                    push(node, dst)
                else:
                    seen[node] += 1
            else:
                relabel(node)
                seen[node] = 0
        if height[node] > old_height:
            nodes.insert(0, nodes.pop(p))
            p = 0
        else:
            p += 1

    return sum(flow[source - 1])


if __name__ == '__main__':
    source, sink = 's', 't'
    graph = DiGraph()
    graph.add_edge('s', 'u', 10)
    graph.add_edge('s', 'v', 5)
    graph.add_edge('u', 'v', 15)
    graph.add_edge('u', 't', 5)
    graph.add_edge('v', 't', 10)
    print(graph)
    print("-" * 80)
    print("Edmonds-Karp Algorithm")
    print("Max Flow:", edmonds_karp(graph, source, sink))
    print("-" * 80)
    print("Push-Relabel Algorithm")
    print("Max Flow:", push_relabel(graph, source, sink))
    print("-" * 80)
