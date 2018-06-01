from collections import Counter

def generate_bag_of_words(words):
    """ Given a list of words,
        return a dictionary of words with associated frequencies
    """
    return Counter(words.split())

def is_first_bag_missing_words(bag1, bag2):
    """ If bag2 contains words that are not in bag1,
        return True
    """
    return len(set(bag2.keys()).difference(bag1.keys())) > 0

def does_magazine_contain_ransom_words(m, n, magazine_str, ransom_str):
    # If our ransom note contains more words than our magazine, 
    # we can't make our note from the magazine
    if n > m:
        return False

    magazine_bag_of_words = generate_bag_of_words(magazine_str)
    ransom_bag_of_words = generate_bag_of_words(ransom_str)

    # If the magazine doesn't contain one of the words in our ransom note,
    # we immediately know that we can't make the note with the words in the magazine
    if is_first_bag_missing_words(magazine_bag_of_words, ransom_bag_of_words):
        return False

    for word, num in ransom_bag_of_words.items():
        if num > magazine_bag_of_words[word]:
            return False

    return True
