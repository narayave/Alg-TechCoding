
# Codefights

def firstNotRepeatingCharacter(s):

    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in s:
        if i in dict:
            if dict[i] == 1:
                return i

    return '_'