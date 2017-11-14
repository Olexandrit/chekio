
def most_frequent(array):
    """
        determines the most frequently occurring string in the sequence.
    """

    from collections import Counter
    word_counts = Counter(array)
    top_three = word_counts.most_common(3)
    print(top_three)

    print(top_three[0][0])

    return top_three[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    #assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    #assert most_frequent(['bi', 'a', 'bi', 'a', 'bi'])
    print('Done')