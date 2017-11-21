def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here

    index_begin = text.find(begin)
    print(index_begin)

    if index_begin == -1:
        index_begin = None

    index_end = text.find(end)
    print(index_end)

    if index_end == -1:
        index_end = None

    word = text[index_begin:index_end]

    word = word.replace(begin,"")
    word = word.replace(end, "")

    print(word)

    return word

if __name__ == '__main__':
    print('Example:')
    #print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    #assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    """assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML" """
    #assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    #assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    #assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')