class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbols = ["?", "!", "%", "'", ",", ".", ";", ":", " "]
        pali = s.lower()
        for i in symbols:
            pali = pali.replace(i, "")
        if len(pali) == 1:
            return True
        print(pali)
        print(pali[::-1])
        if pali == pali[::-1]:
            return True
        else:
            return False