from Contacts import Contacts
from Contacts import Node

def test_add_and_get_count_for_node():
    n = Node()
    n.add_to_count()
    n.add_to_count()
    assert n.get_count() == 2

def test_add_char_to_node_and_retrieve():
    n = Node()
    char = 'a'
    assert n.is_char_in_nodes(char) is False
    n.add_char_to_nodes(char)
    assert n.is_char_in_nodes(char) is True

def test_add_new_contact():
    c = Contacts()
    c.add("test")
    assert c.find("test") == 1

def test_add_new_contacts():
    c = Contacts()
    c.add("test")
    c.add("tad")
    c.add("tester")
    c.add("testing")
    print("FINDING TEST")
    assert c.find("test") == 3
    print("FINDING T")
    assert c.find("t") == 4

def test_add_then_find():
    c = Contacts()
    c.add("a")
    c.add("as")
    c.add("add")
    assert c.find("a") == 3
    c.add("assert")
    c.add("assertation")
    assert c.find("a") == 5
    assert c.find("as") == 3
