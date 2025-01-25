from structures.tree.bst import BinarySearchTree
from structures.tree.commons import _height, _left_rotate, _right_rotate


class AVLTree(BinarySearchTree):

    class _Node(BinarySearchTree._Node):
        def __init__(self, key):
            super().__init__(key)
            self.height = 1

        def update_height(self):
            self.height = max(_height(self.left), _height(self.right)) + 1

        def balance_factor(self):
            return _height(self.left) - _height(self.right)

    def insert(self, key):
        new_node = super()._add(key)
        self._rebalance(new_node)

    def remove(self, key):
        node_to_delete = self._find(self.root, key)
        if node_to_delete:
            parent = node_to_delete.parent
            super()._delete(node_to_delete)
            self._rebalance(parent)

    @staticmethod
    def get_name():
        return "AVL tree"

    def _left_rotate(self, x):
        x, y = _left_rotate(self, x)
        x.update_height()
        y.update_height()

    def _right_rotate(self, x):
        x, y = _right_rotate(self, x)
        x.update_height()
        y.update_height()

    def _rebalance(self, x):
        while x:
            x.update_height()
            if x.balance_factor() > 1:
                if x.left.balance_factor() < 0:
                    self._left_rotate(x.left)
                self._right_rotate(x)
            elif x.balance_factor() < -1:
                if x.right.balance_factor() > 0:
                    self._right_rotate(x.right)
                self._left_rotate(x)
            x = x.parent
