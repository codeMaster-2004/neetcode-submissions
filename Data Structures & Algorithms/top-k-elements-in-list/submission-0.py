class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        sort = sorted(freq.items(), key=lambda item:item[1], reverse=True)
        sorted_ = dict(sort)
        final = []
        for key in sorted_:
            final.append(key)
            k -= 1
            if k == 0:
                break
        return final
