import re
def is_stressful(subj):
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(word), subj.lower())
                for word in ['help', 'asap', 'urgent']))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert is_stressful("Hi") == False, "First"
    #assert is_stressful("I neeed HELP") == True, "Second"
    #assert is_stressful("h!e!l!p") == True
    #assert is_stressful("A.S.A.P.!!") == True
    #assert is_stressful("where are you?!!!!") == True
    #assert is_stressful("UUUURGGGEEEEENT here") == True
    #assert is_stressful("I\u2019m REALLY happy on my vacation!") == False
    assert is_stressful("Heeeeeey!!! I\u2019m having so much fun!\u201d") == False
    print('Done! Go Check it!')
