class DisjointSets:

    def __init__(self, keys=None):
        self.dict = {}
        if keys:
            for key in keys:
                self.add(key)

    class _Node:
        def __init__(self, key):
            self.key = key
            self.parent = None
            self.rank = 0

    def add(self, key):
        if key not in self.dict:
            self.dict[key] = self._Node(key)

    def find(self, x):
        if x not in self.dict:
            return None
        return self._find(self.dict[x])

    def union(self, x, y):
        if x in self.dict and y in self.dict:
            self._join(self.dict[x], self.dict[y])

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def _find(self, node):
        if node.parent is None:
            return node
        node.parent = self._find(node.parent)
        return node.parent

    def _join(self, x, y):
        xr = self._find(x)
        yr = self._find(y)
        if xr == yr:
            return
        elif yr.rank > xr.rank:
            xr.parent = yr
        elif xr.rank > yr.rank:
            yr.parent = xr
        else:
            yr.parent = xr
            xr.rank += 1
