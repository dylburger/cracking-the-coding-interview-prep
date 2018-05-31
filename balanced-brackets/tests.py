from are_brackets_balanced import is_balanced

def test_single_balanced_case():
    assert is_balanced('[]') is True
    assert is_balanced('()') is True
    assert is_balanced('{}') is True

def test_trivial_unbalanced_case():
    assert is_balanced('[') is False
    assert is_balanced('{') is False
    assert is_balanced('(') is False

def test_three_balanced_brackets():
    assert is_balanced('[({})]') is True

def test_complex_balanced_brackets():
    assert is_balanced('[({([])})]') is True

def test_unbalanced_mess():
    assert is_balanced('[({([[[]]}[]]][]') is False
