from structures.base import SetOperations


class Trie(SetOperations):

    def __init__(self):
        self.root = self._Node()

    class _Node:

        def __init__(self, end_of_word=False):
            self.children = {}
            self.end_of_word = end_of_word

        def size(self):
            count = 1 if self.end_of_word else 0
            for child in self.children.values():
                count += child.size()
            return count

    def size(self):
        return self.root.size()

    def contains(self, word):
        node = self.root
        for char in word:
            found = False
            for c in node.children:
                if c == char:
                    node = node.children[c]
                    found = True
                    break
            if not found:
                return False
        return node.end_of_word

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self._Node()
            node = node.children[char]
        node.end_of_word = True

    def remove(self, word: str):
        def _remove(node, word, index):
            if index == len(word):
                if not node.end_of_word:
                    return False
                node.end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            can_delete_child = _remove(node.children[char], word, index + 1)

            if can_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.end_of_word

            return False

        _remove(self.root, word, 0)
