class MaxHeap:
    def __init__(self):
        self.array = []

    def get_value(self, i):
        return self.array[i]

    def set_value(self, i, val):
        self.array[i] = val

    def append(self, val):
        self.array.append(val)

    def get_array_size(self):
        return len(self.array)

    def get_parent_index(self, i):
        return i >> 1

    def get_left_index(self, i):
        return i << 1

    def get_right_index(self, i):
        return (i << 1) + 1

    def get_parent_value(self, i):
        return self.get_value(self.get_parent_index(i))

    def get_left_value(self, i):
        return self.get_value(self.get_left_index(i))

    def get_right_value(self, i):
        return self.get_value(self.get_right_index(i))

    def has_parent(self, i):
        return self.get_parent_index(i) >= 0

    def has_left_child(self, i):
        return self.get_left_index(index) < self.get_array_size()

    def has_right_child(self, i):
        return self.get_right_child(index) < self.get_array_size()

    def swap(self, idx1, idx2):
        tmp = self.get_value(idx1)
        self.set_value(idx1, self.get_value(idx2))
        self.set_value(idx2, tmp)

    def get_root_value(self):
        if self.get_array_size() == 0:
            raise IndexError

        return self.get_value(0)

    def add(self, value):
        index = self.get_array_size()
        self.append(value)
        # If the value at the current index is greater than the parent, swap
        while index > 0 and self.get_value(index) > self.get_parent_value(index):
            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index
