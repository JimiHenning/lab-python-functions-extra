def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here
    set_lst = set(lst)
    new_lst = list(set_lst)
    return (new_lst)


def count_case_f(strng):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    import string
    string_nopunct_nospace = strng.translate(str.maketrans('', '', string.punctuation)).replace(" ","")
    upper_count = 0
    lower_count = 0
    for char in string_nopunct_nospace:
        if char.isupper() == True:
            upper_count += 1
        else:
            lower_count += 1

    return (upper_count, lower_count)


def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    import string
    sentence_nopunct = sentence.translate(str.maketrans('', '', string.punctuation))
    return sentence_nopunct


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    # your code goes here
    sentence_np = remove_punctuation(sentence)
    word_list = sentence_np.split()
    count = len(word_list)
    return count
