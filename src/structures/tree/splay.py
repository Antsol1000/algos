from structures.tree.bst import BinarySearchTree
from structures.tree.commons import _right_rotate, _left_rotate


class SplayTree(BinarySearchTree):

    def contains(self, key):
        node = self._find(self.root, key)
        if node:
            self._splay(node)
        return node is not None

    def insert(self, key):
        new_node = super()._add(key)
        self._splay(new_node)

    def remove(self, key):
        node_to_delete = self._find(self.root, key)
        if node_to_delete:
            self._splay(node_to_delete)
            super()._delete(node_to_delete)

    @staticmethod
    def get_name():
        return "splay tree"

    def _splay(self, x):
        while x.parent is not None:
            if x.parent.parent is None:
                if x.parent.left == x:
                    _right_rotate(self, x.parent)
                else:
                    _left_rotate(self, x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                _right_rotate(self, x.parent.parent)
                _right_rotate(self, x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                _left_rotate(self, x.parent.parent)
                _left_rotate(self, x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.right:
                _right_rotate(self, x.parent)
                _left_rotate(self, x.parent)
            else:
                _left_rotate(self, x.parent)
                _right_rotate(self, x.parent)
