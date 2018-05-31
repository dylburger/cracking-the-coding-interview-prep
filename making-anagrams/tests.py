import string
from FrequencyMap import FrequencyMap, compare_frequency_maps

def test_create_and_validate_frequency_map():
    test_str = 'test'
    f = FrequencyMap(test_str)
    validation_dict = { char : 0 for char in string.ascii_lowercase }
    for char in test_str:
        validation_dict[char] += 1

    assert f.get_frequency_dict() == validation_dict
