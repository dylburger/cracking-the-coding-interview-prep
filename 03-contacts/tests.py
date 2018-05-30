from Contacts import Contacts

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
