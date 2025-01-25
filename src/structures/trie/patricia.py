from structures.base import SetOperations


class PatriciaTrie(SetOperations):
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
        i = 0
        while i < len(word):
            found = False
            for key in node.children:
                if word.startswith(key, i):
                    node = node.children[key]
                    i += len(key)
                    found = True
                    break
            if not found:
                return False
        return node.end_of_word

    def insert(self, word):
        node = self.root
        i = 0
        while i < len(word):
            found = False
            for key in node.children:
                if word.startswith(key, i):
                    node = node.children[key]
                    i += len(key)
                    found = True
                    break
                common_prefix_length = self._common_prefix_length(key, word[i:])
                if common_prefix_length > 0:
                    common_prefix = key[:common_prefix_length]
                    remaining_key = key[common_prefix_length:]
                    remaining_word = word[i + common_prefix_length:]
                    new_node = self._Node()
                    new_node.children[remaining_key] = node.children.pop(key)
                    node.children[common_prefix] = new_node
                    node = new_node
                    if remaining_word:
                        new_node.children[remaining_word] = self._Node(end_of_word=True)
                    else:
                        new_node.end_of_word = True
                    return
            if not found:
                node.children[word[i:]] = self._Node(end_of_word=True)
                return

        node.end_of_word = True

    def remove(self, word: str):
        def _remove(node, word, index):
            if index == len(word):
                if not node.end_of_word:
                    return False
                node.end_of_word = False
                return len(node.children) == 0

            for key in node.children:
                if word.startswith(key, index):
                    can_delete_child = _remove(node.children[key], word, index + len(key))
                    if can_delete_child:
                        del node.children[key]
                        return len(node.children) == 0 and not node.end_of_word
                    return False
            return False

        _remove(self.root, word, 0)

    def _common_prefix_length(self, str1, str2):
        min_length = min(len(str1), len(str2))
        for i in range(min_length):
            if str1[i] != str2[i]:
                return i
        return min_length
