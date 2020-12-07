
# https://leetcode.com/discuss/interview-question/370112/


def kSubstring(in_s, k):
    # 2 pointer method

    # print(in_s, type(in_s))
    # print(k, type(k))

    res = []
    s = -1
    d = k - 1

    while d <= len(in_s) - 1:
        ans = ""
        s += 1
        d += 1
        # print(in_s[s:d], s, d)

        for i in range(s, d):
            # print(s, d)
            if in_s[i] not in ans:
                ans += in_s[i]
            else:
                ans = ""
                break
        if ans not in res and len(ans) == k:
            res.append(ans)

    return res


print(list(kSubstring("awaglknagawunagwkwagl", 4)))
print(list(kSubstring("democracy", 4)))
print(list(kSubstring("tellopatha", 4)))

# ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
# ['wagl', 'aglk', 'glkn', 'lkna', 'knag', 'gawu', 'awun', 'wuna', 'unag', 'nagw', 'agwk', 'kwag']
