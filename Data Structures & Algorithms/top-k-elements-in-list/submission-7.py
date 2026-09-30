class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ret = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        sorted_freq = sorted(freq.items(), key=lambda x:x[1])

        k1 = 0
        for key, value in reversed(sorted_freq):
            ret.append(key)
            k1 += 1
            if k1 == k:
                break
        
        return ret