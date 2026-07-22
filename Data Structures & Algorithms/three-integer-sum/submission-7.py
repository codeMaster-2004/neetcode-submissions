class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        dup = set()
        if n < 3:
            return []

        for i in range(n - 2):
            if nums[i] in dup:
                continue
            dup.add(nums[i])
            ptr = nums[i]

            j = i + 1
            k = n - 1
            while j < k:
                if ptr + nums[j] + nums[k] == 0:
                    res.append([ptr, nums[j], nums[k]])
                    j += 1
                    k -=1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    continue
                if ptr + nums[j] + nums[k] > 0:
                    k -= 1
                if ptr + nums[j] + nums[k] < 0:
                    j += 1
        return res