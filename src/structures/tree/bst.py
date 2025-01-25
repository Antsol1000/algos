from structures.base import SetOperations


class BinarySearchTree(SetOperations):

    def __init__(self):
        self.root = None

    def __iter__(self):
        return self._in_order_traversal(self.root)

    def __repr__(self):
        return f"{self.get_name()}({', '.join(str(x) for x in self)})"

    class _Node:
        def __init__(self, key):
            self.left = self.right = self.parent = None
            self.key = key

        def __repr__(self):
            return f"({self.key})"

    def size(self):
        return sum(1 for _ in self)

    def contains(self, key):
        return self._find(self.root, key) is not None

    def insert(self, key):
        self._add(key)

    def remove(self, key):
        node_to_delete = self._find(self.root, key)
        if node_to_delete:
            self._delete(node_to_delete)

    @staticmethod
    def get_name():
        return "binary search tree"

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def _find(self, x, key):
        while x and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def _add(self, key):
        x = self._Node(key)
        if not self.root:
            self.root = x
        else:
            self._add_child(self.root, x)
        return x

    def _min_node(self, x):
        while x.left is not None:
            x = x.left
        return x

    def _add_child(self, x, y):
        while True:
            if y.key < x.key:
                if x.left is None:
                    x.left = y
                    y.parent = x
                    break
                x = x.left
            else:
                if x.right is None:
                    x.right = y
                    y.parent = x
                    break
                x = x.right

    def _delete(self, z):
        if not z.left:
            self._transplant(z, z.right)
        elif not z.right:
            self._transplant(z, z.left)
        else:
            y = self._min_node(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent
