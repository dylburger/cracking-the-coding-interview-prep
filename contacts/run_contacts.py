from Contacts import Contacts

def parse_input():
    """ Return a list of operations and associated strings to perform
    """
    operations = []
    n = int(input())

    for n_itr in range(n):
        opContact = input().split()
        operations.append([opContact[0], opContact[1]])

    return operations

def process_operations(operations):
    c = Contacts()
    for op in operations:
        if op[0] == 'add':
            c.add(op[1])
        if op[0] == 'find':
            print(c.find(op[1]))

if __name__ == '__main__':
    operations = parse_input()
    process_operations(operations)
