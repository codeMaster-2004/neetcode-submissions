class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        start = 1
        comp[nums[0]] = 0
        for i, num in enumerate(nums[start:], start=1):
            if target - nums[i] in comp:
                return [comp.get(target - nums[i]), i]
            else:
                comp[nums[i]] = i