def checkio(str_number, radix):
    import string
    letter = string.ascii_uppercase
    num = string.digits
    for ch in str_number:
        if ch in letter:
            if letter.index(ch) + 10 >= radix:
                return -1
        elif ch in num:
            if int(ch) >= radix:
                return -1

    print(int(str_number, radix))
    return int(str_number, radix)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")