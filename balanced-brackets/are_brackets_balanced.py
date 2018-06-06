import re


def is_left_bracket(char):
    """ Given a character,
        return the match object if the character is a left bracket, else None
    """
    pattern = r'[\[{(]'
    return re.search(pattern, char)


def is_right_bracket(char):
    """ Given a character,
        return the match object if the character is a right bracket, else None
    """
    pattern = r'[\]})]'
    return re.search(pattern, char)


def get_matching_left_bracket(char):
    """ Given a right bracket, return the matching left bracket
    """
    left_bracket_dict = {
        '}': '{',
        ']': '[',
        ')': '(',
    }

    return left_bracket_dict[char]


def is_balanced(bracket_string):
    """ Given a string of bracket characters - (), {} or [] -
        return true if the string of brackets are "balanced", else False
    """
    stack = []
    balanced = True
    for char in bracket_string:
        if is_left_bracket(char):
            stack.append(char)
            continue

        if is_right_bracket(char):
            # If the stack is empty, we have a right bracket without
            # a matching left bracket
            if len(stack) == 0:
                balanced = False
                break

            # The last element of our stack should be the left bracket
            # that matches the current right bracket. If not, the brackets
            # are unbalanced
            if not stack.pop() == get_matching_left_bracket(char):
                balanced = False
                break

    if balanced is False:
        return False

    return len(stack) == 0
