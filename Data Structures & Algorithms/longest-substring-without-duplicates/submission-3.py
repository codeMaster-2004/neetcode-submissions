class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 1
        char_set = set()
        if len(s) < 1:
            return 0
        for r in range(len(s)):
            if s[r] in char_set:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
            max_length = max(len(char_set), max_length)
        return max_length