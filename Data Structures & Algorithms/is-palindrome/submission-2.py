import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "").lower()
        strin_g = ""
        for i in range(len(st)):
            if st[i].isalnum():
                strin_g += st[i]
        rs = ""
        rs = strin_g[::-1]

        return rs == strin_g