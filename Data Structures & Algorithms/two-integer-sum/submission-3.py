class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        start = 1
        comp[nums[0]] = 0
        print(f"comp before is {comp}")
        for i, num in enumerate(nums[start:], start=1):
            print(f"i is {i}")
            print(f"num is {num}")
            print(f"comp is {comp}")
            print(f"result of if statement {comp.get(target - nums[i])}")
            if target - nums[i] in comp:
                return [comp.get(target - nums[i]), i]
            else:
                comp[nums[i]] = i
            print(f"comp after is {comp}")