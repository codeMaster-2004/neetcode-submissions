class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        reslist = []
        resdict = {}
        for word in strs:
            word1 = "".join(sorted(word))
            if word1 not in resdict:
                resdict[word1] = [word]
            else:
                resdict[word1].append(word)
        for key in resdict:
            reslist.append(resdict[key])
        return reslist