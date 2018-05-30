class Node:
    def __init__(self):
        self.count = 0
        self.nodes = {}

    def is_char_in_nodes(self, char):
        return char in self.nodes

    def add_char_to_nodes(self, char):
        self.nodes[char] = Node()

    def add_to_count(self):
        self.count += 1


class Contacts:
    def __init__(self):
        self.contacts = Node()

    def __repr__(self):
        return '%s' % self.contacts

    def add(self, contact):
        chars = list(contact)

        def add_string_to_trie(node, remaining_chars):
            print("Remaining characters: %s" % remaining_chars)
            if len(remaining_chars) == 0:
                node.add_to_count()
                return

            next_char, *rest = remaining_chars

            if not node.is_char_in_nodes(next_char):
                print("Node for %s does not yet exist" % next_char)
                node.add_char_to_nodes(next_char)

            add_string_to_trie(node.nodes[next_char], rest)

        add_string_to_trie(self.contacts, chars)


    def find(self, partialStr):
        """ Navigate down our trie, checking whether we have a node (partial match) at each level
            If we reach the end of our partialStr, recurse down our trie to count how many matches
            we have below that
        """
        def count_words(node, count):
            print("Count so far: %s" % count)
            # Add any exact matches
            print("Adding %s to count" % node.count)
            count += node.count

            print("Characters at this point in trie: %s" % node.nodes.keys())
            for char in node.nodes.keys():
                print("Processing sub-trie for %s" % char)
                return count_words(node.nodes[char], count)

            return count

        def find_node_at_str(node, remaining_chars):
            print("Remaining characters: %s" % remaining_chars)
            if len(remaining_chars) == 0:
                print("No more remaining characters. Count from here on down!")
                count = count_words(node, 0)
                print("FINAL COUNT: %s" % count)
                return count

            next_char, *rest = remaining_chars
            if not node.is_char_in_nodes(next_char):
                return 0

            return find_node_at_str(node.nodes[next_char], rest)

        return find_node_at_str(self.contacts, partialStr)
