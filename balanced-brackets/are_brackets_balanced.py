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

def is_balanced(brackets):

    def are_brackets_balanced(bracket_string, stack):
        """ Given a string of bracket characters - (), {} or [] -
            return true if the string of brackets are "balanced", else False
        """
        if len(bracket_string) == 0:
            return len(stack) == 0

        next_char, *rest = bracket_string

        if is_left_bracket(next_char):
            stack.append(next_char)
            return are_brackets_balanced(rest, stack)

        if is_right_bracket(next_char):
            # If the stack is empty, we have a right bracket without 
            # a matching left bracket
            if len(stack) == 0:
                return False

            # The last element of our stack should be the left bracket
            # that matches the current right bracket. If not, the brackets
            # are unbalanced
            if not stack.pop() == get_matching_left_bracket(next_char):
                return False

            return are_brackets_balanced(rest, stack)

    return are_brackets_balanced(brackets, [])
