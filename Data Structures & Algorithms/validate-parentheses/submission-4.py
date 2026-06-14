class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ref_dict = {"{":"}", "[":"]", "(":")"}
        stack = []
        for char in s:
            if char in ref_dict:
                stack.append(char)
            else:
                if (not stack) or (ref_dict[stack.pop()] != char):
                    return False
        return len(stack) == 0
                