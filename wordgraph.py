"""WordGraph class"""

from collections import deque


class WordGraph:
    """A graph class that maps a word to words that differ from it
    by just one letter.
    """

    def __init__(self, words=None):
        self.nodes = {}
        if words:
            for word in words:
                self.add_node(word)

    @staticmethod
    def adjacent(word1, word2):
        """Check if two words differ by just one letter."""
        if len(word1) != len(word2):
            return False
        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return True

    def add_node(self, word):
        """Add a new word with its 'neighbours' to the graph updating relations
        of existing nodes.
        """
        if word in self.nodes:
            return
        neighbours = set()
        for node in self.nodes:
            if self.adjacent(node, word):
                self.nodes[node].add(word)
                neighbours.add(node)
        self.nodes[word] = neighbours

    def ladder(self, start, end):
        """Find a chain of other words to link start and end, in which two
        adjacent words differ by one letter. Return None if not found.
        """
        for word in (start, end):
            if word not in self.nodes:
                print(f'{word} is not in the wordlist.')
                return

        if start == end:
            return

        queue = deque([start])
        passed = set()
        got_from = {start: None}  # map a word to the preceding one
        success = False

        while queue:
            current_word = queue.popleft()
            if current_word in passed:
                continue
            if end in self.nodes[current_word]:
                got_from[end] = current_word
                success = True
                break
            else:
                passed.add(current_word)
                queue.extend(self.nodes[current_word])
                for word in self.nodes[current_word]:
                    if word not in got_from:  # prevent overwriting
                        got_from[word] = current_word

        if not success:
            return
        backward_chain = [end]
        previous = got_from[end]
        while previous:
            backward_chain.append(previous)
            previous = got_from[previous]
        return backward_chain[::-1]
