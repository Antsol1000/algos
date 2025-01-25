from structures.tree.bst import BinarySearchTree
from structures.tree.commons import RED, BLACK, _left_rotate, _right_rotate, _left, _right, _color, _parent, _set_color


class RedBlackTree(BinarySearchTree):

    class _Node(BinarySearchTree._Node):
        def __init__(self, key, color=RED):
            super().__init__(key)
            self.color = color

        def __repr__(self):
            return f"({self.key}: {self.color})"

    def insert(self, key):
        new_node = super()._add(key)
        self._insert_fixup(new_node)

    def remove(self, key):
        node_to_delete = self._find(self.root, key)
        if node_to_delete:
            self._delete(node_to_delete)

    @staticmethod
    def get_name():
        return "red-black tree"

    def _delete(self, y):
        if y.left and y.right:
            s = self._min_node(y.right)
            y.key = s.key
            y = s

        x = y.left if y.left else y.right
        if x:
            x.parent = y.parent
            if not y.parent:
                self.root = x
            elif y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
            y.left = y.right = y.parent = None
            if y.color == BLACK:
                self._delete_fixup(x)
        elif not y.parent:
            self.root = None
        else:
            if y.color == BLACK:
                self._delete_fixup(y)
            if y.parent:
                if y == y.parent.left:
                    y.parent.left = None
                else:
                    y.parent.right = None
                y.parent = None

    def _left_rotate(self, x):
        if x:
            _left_rotate(self, x)

    def _right_rotate(self, x):
        if x:
            _right_rotate(self, x)

    def _insert_fixup(self, z):
        while z.parent and z.parent.color == RED:
            if _parent(z) == _left(_parent(_parent(z))):
                y = _right(_parent(_parent(z)))
                if _color(y) == RED:
                    _set_color(_parent(z), BLACK)
                    _set_color(y, BLACK)
                    _set_color(_parent(_parent(z)), RED)
                    z = _parent(_parent(z))
                else:
                    if z == _right(_parent(z)):
                        z = _parent(z)
                        self._left_rotate(z)
                    _set_color(_parent(z), BLACK)
                    _set_color(_parent(_parent(z)), RED)
                    self._right_rotate(_parent(_parent(z)))
            else:
                y = _left(_parent(_parent(z)))
                if _color(y) == RED:
                    _set_color(_parent(z), BLACK)
                    _set_color(y, BLACK)
                    _set_color(_parent(_parent(z)), RED)
                    z = _parent(_parent(z))
                else:
                    if z == _left(_parent(z)):
                        z = _parent(z)
                        self._right_rotate(z)
                    _set_color(_parent(z), BLACK)
                    _set_color(_parent(_parent(z)), RED)
                    self._left_rotate(_parent(_parent(z)))
        self.root.color = BLACK

    def _delete_fixup(self, x):
        while x != self.root and _color(x) == BLACK:
            if x == _left(_parent(x)):
                w = _right(_parent(x))
                if _color(w) == RED:
                    _set_color(w, BLACK)
                    _set_color(_parent(x), RED)
                    self._left_rotate(_parent(x))
                    w = _right(_parent(x))
                if _color(_left(w)) == BLACK and _color(_right(w)) == BLACK:
                    _set_color(w, RED)
                    x = _parent(x)
                else:
                    if _color(_right(w)) == BLACK:
                        _set_color(_left(w), BLACK)
                        _set_color(w, RED)
                        self._right_rotate(w)
                        w = _right(_parent(x))
                    _set_color(w, _color(_parent(x)))
                    _set_color(_parent(x), BLACK)
                    _set_color(_right(w), BLACK)
                    self._left_rotate(_parent(x))
                    x = self.root
            else:
                w = _left(_parent(x))
                if _color(w) == RED:
                    _set_color(w, BLACK)
                    _set_color(_parent(x), RED)
                    self._right_rotate(_parent(x))
                    w = _left(_parent(x))
                if _color(_right(w)) == BLACK and _color(_left(w)) == BLACK:
                    _set_color(w, RED)
                    x = _parent(x)
                else:
                    if _color(_left(w)) == BLACK:
                        _set_color(_right(w), BLACK)
                        _set_color(w, RED)
                        self._left_rotate(w)
                        w = _left(_parent(x))
                    _set_color(w, _color(_parent(x)))
                    _set_color(_parent(x), BLACK)
                    _set_color(_left(w), BLACK)
                    self._right_rotate(_parent(x))
                    x = self.root
        _set_color(x, BLACK)


if __name__ == '__main__':
    def repr(tree, node, depth=0):
        if node is None:
            return ""
        result = ""
        if node.right is not None:
            result += repr(tree, node.right, depth + 1)
        result += "\t" * depth + str(node) + "\n"
        if node.left is not None:
            result += repr(repr, node.left, depth + 1)
        return result


    t = RedBlackTree()
    for n in range(1, 11):
        t.insert(n)
    print(repr(t, t.root))
    print("\n")
    for n in range(1, 6):
        t.remove(n)
        print(repr(t, t.root))
        print("\n")
