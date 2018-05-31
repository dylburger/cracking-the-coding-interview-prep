import string

class FrequencyMap:
    def __init__(self, user_str):
        """ Given a string, generate a dictionary of character frequencies
            Constraint: our string contains only lowercase characters a-z
        """
        self.frequency_map = { char : 0 for char in string.ascii_lowercase }
        for char in user_str:
            self.frequency_map[char] += 1

    def get_frequency_dict(self):
        return self.frequency_map


def compare_frequency_maps(freq_map_1, freq_map_2):
    """ Given two frequency maps,
        return the absolute value of the difference between pairwise frequencies
        (e.g. if the first map has 2 occurrences of a and the second map has 4, return 2)
    """
    freq_dict_1 = freq_map_1.get_frequency_dict()
    freq_dict_2 = freq_map_2.get_frequency_dict()

    sum_of_differences = 0
    for char, freq in freq_dict_1:
        sum_of_differences += abs(freq_dict_1[char] - freq_dict_2[char])

    return sum_of_differences
