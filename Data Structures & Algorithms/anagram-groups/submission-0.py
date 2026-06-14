class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            sort_ = ''.join(sorted(s))
            if sort_ not in dic:
                dic[sort_] = [s]
            else:
                dic[sort_].append(s)

        return list(dic.values())