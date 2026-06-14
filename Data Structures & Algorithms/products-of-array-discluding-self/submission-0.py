class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            print("after output[i] = pre:", output, i)
            pre *= nums[i]
            print("after pre *= output[i]:", pre, i)

        post = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= post
            print("after output[i] = post:", output, i)
            post *= nums[i]
            print("after post *= output[i]:", post, i)

        return output