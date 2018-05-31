import pytest
from rotLeft import rotLeft

def test_no_input():
    with pytest.raises(AssertionError):
        rotLeft(0, 0)

def test_one_element_input():
    a = [1]
    d = 1
    assert rotLeft(a, d) == a

def test_d_larger_than_len_a():
    a = [1]
    d = 2
    with pytest.raises(AssertionError):
        rotLeft(a, d)

def test_one_left_rotation():
    a = [1, 2, 3]
    d = 1
    left_rotated_list = [2, 3, 1]
    assert rotLeft(a, d) == left_rotated_list

def test_two_left_rotations():
    a = [1, 2, 3]
    d = 2
    left_rotated_list = [3, 1, 2]
    assert rotLeft(a, d) == left_rotated_list
