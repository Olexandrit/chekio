def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    print(phrases)
    phrases2 = []
    for word in phrases:
        # print(word)
        word2 = word.replace("right", "left")
        phrases2.append(word2)
        # print(word2)

    print(phrases2)

    words = ",".join(phrases2)

    print(words)
    return words


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    # assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    # assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    # assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
