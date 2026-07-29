class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            print(f"after initializing m to {m}")
            if target == nums[m]:
                print("after entering nums[m] equality check")
                return m
            elif nums[m] > target:
                print("after entering nums[m] > target equality check")
                r = m - 1
            elif nums[m] < target:
                print("after entering nums[m] < target equality check")
                l = m + 1
        
        return -1