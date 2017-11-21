def checkio(first, second):
    str = first + "," + second

    mas_str = str.split(",")
    print("mas_str= ",mas_str)

    mas_find = set(mas_str)
    print("mas_find= ",mas_find)

    mas_result = []
    for word in mas_find:
        word_count = mas_str.count(word)
        if word_count >= 2:
            mas_result.append(word)

    mas_result.sort()
    print(mas_result)

    result = ','.join(mas_result)
    print(result)

    return result

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    #assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
