from structures.base import SetOperations


class SuffixTree(SetOperations):

    def __init__(self):
        self.root = self._Node()

    class _Node:
        def __init__(self):
            self.children = {}
            self.end_of_word = False

        def size(self):
            count = 1 if self.end_of_word else 0
            for child in self.children.values():
                count += child.size()
            return count

    def size(self):
        return self.root.size()

    def contains(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = self._Node()
            current = current.children[char]
        if not current.end_of_word:
            current.end_of_word = True

    def remove(self, word):
        def _remove(node, word, depth):
            if depth == len(word):
                if not node.end_of_word:
                    return False
                node.end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete_child = _remove(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0
            return False

        _remove(self.root, word, 0)
