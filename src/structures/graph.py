import random


class Graph:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.neighbors = []

        def __iter__(self):
            return iter(self.neighbors)

        def __repr__(self):
            return ", ".join(str(e) for e in self.neighbors)

    class _Edge:
        def __init__(self, dst, val):
            self.dst = dst
            self.val = val

        def __iter__(self):
            return iter([self.dst, self.val])

        def __repr__(self):
            r = f"{self.dst}"
            if self.val:
                r += f"({self.val})"
            return r

    def __init__(self):
        self.nodes = {}

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, key):
        return self.nodes[key]

    def __repr__(self):
        return "\n".join([f"{n}: {self[n]}" for n in self])

    def add_node(self, key, val=None):
        self.nodes[key] = self._Node(val)

    def remove_node(self, key):
        del self.nodes[key]
        for n in self:
            self.nodes[n].neighbors = [e for e in self.nodes[n].neighbors if e.dst != key]

    def add_edge(self, src, dst, val=None):
        if src not in self.nodes:
            self.add_node(src)
        if dst not in self.nodes:
            self.add_node(dst)
        self._add_edge(src, dst, val)

    def transpose(self):
        g = self.__class__()
        for n in self:
            g.add_node(n)
        for n in self:
            for e in self[n]:
                g.add_edge(e.dst, n, e.val)
        return g

    def get_node_keys(self):
        return self.nodes.keys()

    def get_edges(self):
        return [(n, e.dst, e.val) for n in self for e in self[n]]

    def __copy__(self):
        g = self.__class__()
        for n in self:
            g.add_node(n)
        for n in self:
            for e in self[n]:
                g.add_edge(n, e.dst, e.val)
        return g

    def _add_edge(self, src, dst, val):
        self.nodes[src].neighbors.append(self._Edge(dst, val))
        if src != dst:
            self.nodes[dst].neighbors.append(self._Edge(src, val))


class DiGraph(Graph):

    def _add_edge(self, src, dst, val):
        self.nodes[src].neighbors.append(self._Edge(dst, val))


def rand_graph(vertices_number, edges_max, weight_max):
    g = Graph()
    for i in range(1, vertices_number + 1):
        g.add_node(i)
        r = random.randint(1, edges_max)
        j = 1
        while j <= i - 1 and j <= r:
            v = random.randint(1, i - 1)
            w = random.randint(1, weight_max)
            g.add_edge(v, i, w)
            j += 1
    return g
