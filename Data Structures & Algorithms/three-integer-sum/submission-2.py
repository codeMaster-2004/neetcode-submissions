class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        for i in range(len(nums) - 1):
            out = nums[i]
            seen = set()
            for j in range (i + 1, len(nums)):
                comp = -out - nums[j]
                if comp in seen:
                    ret.add(tuple(sorted((nums[i], nums[j], comp))))
                seen.add(nums[j])
        return [list(i) for i in ret]


