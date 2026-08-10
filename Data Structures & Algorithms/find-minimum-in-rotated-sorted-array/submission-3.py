class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = len(nums) // 2
        r = len(nums) - 1
        l = 0

        if len(nums) < 2:
            return nums[0]
        while m <= r:
            if nums[m] > nums[r]:
                l = m
                m = (m+r+1) // 2
            else:
                if nums[m - 1] > nums[m]:
                    return nums[m]
                else:
                    r = m
                    m = (l + m) // 2