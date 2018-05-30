class Contacts:
    def __init__(self):
        self.contacts = set()

    def add(self, contact):
        self.contacts.add(contact)

    def find(self, partialStr):
        matches = [c for c in self.contacts if c.startswith(partialStr)]
        return len(matches)
