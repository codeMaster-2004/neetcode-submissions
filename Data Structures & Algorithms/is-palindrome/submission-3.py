class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "")
        st = st.lower()
        i, j = 0, len(st) - 1

        while j >= i:
            if st[i].isalnum() and st[j].isalnum():
                if st[i] == st[j]:
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
            if st[j].isalnum() == False:
                j -= 1
                continue
            if st[i].isalnum() == False:
                i += 1
                continue
        return True