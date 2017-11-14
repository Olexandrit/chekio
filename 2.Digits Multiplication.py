def checkio(number):
    number_str = str(number)
    print(number_str)
    str_not_null = number_str.replace("0", "")
    print(str_not_null)

    cn = 1
    for word in str_not_null:
        n = int(word)
        cn = cn * n

    print(cn)
    return cn


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
