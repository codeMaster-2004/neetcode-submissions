class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1
            
            word_tup = tuple(count)

            if word_tup in group:
                group[word_tup].append(word)
            else:
                group[word_tup] = [word]
        ret = []
        for _, value in group.items():
            ret.append(value)
        
        return ret