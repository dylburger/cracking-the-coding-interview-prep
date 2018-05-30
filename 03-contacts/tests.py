from Contacts import Contacts

def test_add_new_contact():
    c = Contacts()
    c.add("test")
    assert c.find("test") == 1

def test_add_duplicate_contact():
    c = Contacts()
    c.add("test")
    c.add("test")
    assert c.find("test") == 1
