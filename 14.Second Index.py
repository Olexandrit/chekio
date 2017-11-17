def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    try:
        find_symbol_index = text.rindex(symbol)
        print(find_symbol_index)
        return find_symbol_index

    except ValueError:
        return None

if __name__ == '__main__':
    print('Example:')
    #print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert second_index("sims", "s") == 3, "First"
    #assert second_index("find the river", "e") == 12, "Second"
    #assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    #assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')