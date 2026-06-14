class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        retS, retT = {}, {}
        for i in range(len(s)):
            retS[s[i]] = retS.get(s[i], 0) + 1
            retT[t[i]] = retT.get(t[i], 0) + 1
        return retS == retT
                
        