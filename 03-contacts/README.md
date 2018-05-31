[Link to problem statement](https://www.hackerrank.com/challenges/ctci-contacts/problem)

Tries can be really useful in problems where you must compare some set of words against a list of words (word validation problems).

This solution requires us to retrieve a count of words "below" a given point in our trie (i.e. given a partial match "a", we need to return a count of words that start with "a" that have been previously added to our trie). Since we must traverse the trie to create our words already (adding a node for each character in our word), we increment the `count_below_this_point` attribute tied to a given node each time we encounter that node:

    def __init__(self):
        self.count_below_this_point = 0
        self.nodes = {}

    def add_to_count(self):
        self.count_below_this_point += 1

This ensures we don't have to recurse down through the tree when performing "find" operations. We must only look up the value of the `count_below_this_point` for the node matching our partial string and return that.

An example may help make this more clear. Let's add the word "a" to our trie first. We first attach a reference to an "a" node from our root, incrementing the `count_below_this_point` attribute for that node:

    node : count

    *
    |
    a : 1

Next, let's add the word "add". We already have an "a" node attached to our root, **but we increment the `count_below_this_point` attribute at this node, since there are now two words that begin with "a"** ("a" and "add"). We continue creating new nodes or our remaining letters and incrementing the count associated with them:

    *
    |
    a : 2
    |
    d : 1
    |
    d : 1

Finally, let's add the word "addition":


    *
    |
    a : 3
    |
    d : 2
    |
    d : 2
    |
    i : 1
    |
    t : 1
    |
    i : 1
    |
    o : 1
    |
    n : 1
