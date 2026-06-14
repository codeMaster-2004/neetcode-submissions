class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        target = {}
        mapp = {}

        final = False
        for i, j in zip(s, t):
            if (i not in target or j not in mapp): 
                target[i] = 1
                mapp[j] = 1
            else:
                target[i] += 1
                mapp[j] += 1
        if (mapp == target):
            final = True
        
        return final
        