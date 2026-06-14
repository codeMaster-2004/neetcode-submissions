import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = ""
        for char in s:
            print(f"character {char}")
            if char.isalnum():
                original += char
            print(f"original {original}")
        original = original.lower()
        ret = original[::-1]
        
        return ret == original