import string
from FrequencyMap import FrequencyMap, compare_frequency_maps

def test_create_and_validate_frequency_map():
    test_str = 'test'
    f = FrequencyMap(test_str)
    validation_dict = { char : 0 for char in string.ascii_lowercase }
    for char in test_str:
        validation_dict[char] += 1

    assert f.get_frequency_dict() == validation_dict

def test_compare_freq_maps():
    f1 = FrequencyMap('test')
    f2 = FrequencyMap('tseting')
    assert compare_frequency_maps(f1, f2) == 3

def test_compare_exact_anagrams():
    f1 = FrequencyMap('test')
    f2 = FrequencyMap('tset')
    assert compare_frequency_maps(f1, f2) == 0

def test_compare_words_with_no_chars_in_common():
    f1 = FrequencyMap('abc')
    f2 = FrequencyMap('def')
    assert compare_frequency_maps(f1, f2) == 6

def test_all_but_one_char_in_common():
    f1 = FrequencyMap('abc')
    f2 = FrequencyMap('bcd')
    assert compare_frequency_maps(f1, f2) == 2

def test_lots_of_deletions():
    f1 = FrequencyMap('abc')
    f2 = FrequencyMap('abcdefghi')
    assert compare_frequency_maps(f1, f2) == 6
