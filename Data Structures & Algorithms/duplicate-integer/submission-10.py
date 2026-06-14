class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for num in nums:
            res.add(num)
        print(f"len of res: {res}")
        if len(res) == len(nums):
            return False
        else:
            return True