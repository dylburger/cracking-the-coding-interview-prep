from ransom_note import *

def test_are_we_missing_words():
    str1 = "this is a test"
    str2 = "this is another test"
    bag1 = generate_bag_of_words(str1)
    bag2 = generate_bag_of_words(str2)
    assert is_first_bag_missing_words(bag1, bag2) is True

def test_does_magazine_contain_ransom_words_true():
    str1 = "this is a test"
    str2 = "this test"
    assert does_magazine_contain_ransom_words(4, 2, str1, str2) is True

def test_ransom_note_contains_more_words_than_magazine():
    str1 = "this test"
    str2 = "this is a test"
    assert does_magazine_contain_ransom_words(2, 4, str1, str2) is False

def test_ransom_note_is_missing_words():
    str1 = "this is a test and another test and another"
    str2 = "this is a test blah"
    assert does_magazine_contain_ransom_words(9, 5, str1, str2) is False

def test_ransom_note_has_too_many_of_one_word():
    str1 = "this is a test and another test and another"
    str2 = "test test test"
    assert does_magazine_contain_ransom_words(9, 3, str1, str2) is False
