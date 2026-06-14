class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resdict = {}

        for n in nums:
            if n not in resdict:
                resdict[n] = 1
            else:
                resdict[n] += 1
        freq = sorted(resdict, key=lambda x: resdict[x], reverse=True)
        reslist = []
        for i in range(k):
            reslist.append(freq[i])
        return reslist