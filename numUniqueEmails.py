
# Leetcode mock interview - https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        mails = []
        for e in emails:

            es = e.split("@")
            # print(es)
            localname = es[0].split("+")[0].replace(".", "")

            email = f"{localname}@{es[1]}"
            # print(email)
            if email not in mails:
                mails.append(email)

        return len(mails)