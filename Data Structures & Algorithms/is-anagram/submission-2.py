class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ret = {}
        count = 0
        for c in s:
            ret[c] = ret.get(c, 0) + 1
        
        print(f"ret is {ret}")
        for c in t:
            if c not in ret:
                return False
            ret[c] -= 1
            if ret[c] < 0:
                return False

        return True
                
        