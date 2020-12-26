
# https://leetcode.com/discuss/interview-question/928806/


def get_count(sin, pattern):
    """
        Runs through 1 section of the string to get count of pattern
    """

    pattern_len = len(pattern)
    s = 0
    d = pattern_len
    count = 0

    # print(sin, pattern)

    while d <= len(sin):

        cut = sin[s:d]
        # print(cut)
        if cut == pattern:
            count += 1
            s += 1
            d += 1
        else:
            s += 1
            d += 1

    return count


def recognize_pattern(input):
    """
        Returns final result, with counts of string and final sum
    """

    # print(input.split(";"))

    first_split = input.split(";")
    pattern = first_split[0]
    strs = first_split[1].split("|")
    res_list = []

    print(pattern, strs)
    if len(pattern) == 0:
        res_list = [0]*len(strs)
    else:
        for chars in strs:
            res_list.append(get_count(chars, pattern))

    addedvals = sum(res_list)
    res_list.append(addedvals)
    res_str = "|".join([str(i) for i in res_list])

    return res_str


if __name__ == '__main__':

    testcases = [
        "bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        "aa;aaaakjlhaa|aaadsaaa|easaaad|sa",
        "b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        ";bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32"
    ]

    answers = [
        "3|2|1|2|8",
        "4|4|2|0|10",
        "4|2|3|2|11",
        "0|0|0|0|0"
    ]

    res1 = recognize_pattern(testcases[0])
    print(res1, answers[0])

    res2 = recognize_pattern(testcases[1])
    print(res2, answers[1])

    res3 = recognize_pattern(testcases[2])
    print(res3, answers[2])

    res4 = recognize_pattern(testcases[3])
    print(res4, answers[3])
