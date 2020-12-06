small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    #assigns book_title function argument to list lst_of_words by splitting it between spaces and changes it to lowercase
    lst_of_words = title.lower().split()
    
    #retrieves the first element of lst_of_words list and affects it to new_title 
    new_title = lst_of_words.pop(0)
    
    #takes the first string of new_tile and puts it to uppercase and concatenate with the rest of the string
    new_title = new_title[0].upper() + new_title[1:]
    
    for word in lst_of_words:
        prep_word = False
        for prep in small_words:
            if prep == word:
                new_title += ' '+word
                prep_word = True
                break
        if prep_word:
            continue
        new_title += ' '+word[0].upper()+word[1:]
    return new_title

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()