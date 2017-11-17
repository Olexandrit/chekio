def say_hi(name, age):
    """
        Hi!
    """
    # your code here
    text = "Hi. My name is {name} and I'm {age} years old".format(name = name, age = age)
    print(text)
    return text

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #say_hi("Alex", 32)
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    #print('Done. Time to Check.')