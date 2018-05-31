class Node:
    def __init__(self):
        self.count_below_this_point = 0
        self.nodes = {}

    def is_char_in_nodes(self, char):
        return char in self.nodes

    def get_count(self):
        return self.count_below_this_point

    def add_char_to_nodes(self, char):
        self.nodes[char] = Node()

    def add_to_count(self):
        self.count_below_this_point += 1


class Contacts:
    def __init__(self):
        self.contacts = Node()

    def __repr__(self):
        return '%s' % self.contacts

    def add(self, contact):
        chars = list(contact)

        def add_string_to_trie(node, remaining_chars):
            if len(remaining_chars) == 0:
                node.add_to_count()
                return

            node.add_to_count()

            next_char, *rest = remaining_chars

            if not node.is_char_in_nodes(next_char):
                node.add_char_to_nodes(next_char)

            add_string_to_trie(node.nodes[next_char], rest)

        add_string_to_trie(self.contacts, chars)


    def find(self, partialStr):
        """ Navigate down our trie, checking whether we have a node (partial match) at each level
            If we reach the end of our partialStr, get the count at this node
        """
        def count_words(node):
            return node.get_count()

        def find_node_at_str(node, remaining_chars):
            if len(remaining_chars) == 0:
                return count_words(node)

            next_char, *rest = remaining_chars
            if not node.is_char_in_nodes(next_char):
                return 0

            return find_node_at_str(node.nodes[next_char], rest)

        return find_node_at_str(self.contacts, partialStr)
