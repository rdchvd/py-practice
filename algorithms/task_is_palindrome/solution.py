import re


def is_palindrome(sentence: str):
    """
    Find if the sentence in the natural order is the same as the sentence in reversed one.
    :param sentence: the sentence being checked
    :return: bool: True, if the sentence is palindrome, False otherwise.
    """
    sentence = re.sub("[^A-Z]", "", sentence, 0, re.IGNORECASE).lower()
    return sentence == sentence[::-1]
