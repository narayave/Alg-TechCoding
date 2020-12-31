
# leetocde mock interview question
# https://leetcode.com/problems/license-key-formatting/


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.upper()
        slist = S.split("-")
        if "" in slist:
            slist.remove("")

        joined = "".join(slist)
        mod_K = len(joined) % K
        first_section = joined[:mod_K]
        single_str = joined[mod_K:]

        i = 0
        ns = [first_section]

        while len(single_str) >= K:
            newset = single_str[0:K]
            ns.append(newset)
            single_str = single_str[K:]

        if "" in ns:
            ns.remove("")
        print(f"ns - {ns}")
        return "-".join(ns)
