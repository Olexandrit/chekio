def checkio(time_string):

    time_list = time_string.split(":")
    print(time_list)

    h1 = "{0:b}".format(int(time_list[0].rjust(2, "0")[0])).rjust(4, "0")[-2:].replace("1","-").replace("0",".")
    h2 = "{0:b}".format(int(time_list[0].rjust(2, "0")[1])).rjust(4, "0")[-4:].replace("1","-").replace("0",".")

    m1 = "{0:b}".format(int(time_list[1].rjust(2, "0")[0])).rjust(4, "0")[-3:].replace("1","-").replace("0",".")
    m2 = "{0:b}".format(int(time_list[1].rjust(2, "0")[1])).rjust(4, "0")[-4:].replace("1","-").replace("0",".")

    s1 = "{0:b}".format(int(time_list[2].rjust(2, "0")[0])).rjust(4, "0")[-3:].replace("1","-").replace("0",".")
    s2 = "{0:b}".format(int(time_list[2].rjust(2, "0")[1])).rjust(4, "0")[-4:].replace("1","-").replace("0",".")

    morse = h1 + " " + h2 + " : " + m1 + " " + m2 + " : " + s1 + " " + s2
    print(morse)

    return morse

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    #checkio("10:37:49")