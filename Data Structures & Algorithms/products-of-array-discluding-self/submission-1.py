class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pre = 0
        suf = 0
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                print(f"prefix array at 0th append {prefix}")
            if i == 1:
                pre = nums[0]
                print(f"variable pre: {pre}")
                prefix.append(pre)
                print(f"prefix array at 1st append {prefix}")
            if i >= 2:
                pre = pre * nums[i - 1]
                print(f"variable pre: {pre}")
                prefix.append(pre)
                print(f"prefix array at nth append {prefix}")
        new_arr = nums[::-1]
        # [2, 3, 4, 5] -> [5, 4, 3, 2]
        for i in range(len(nums)):
            if i == 0:
                suffix.append(1)
                print(f"suffix array at 0th append {suffix}")
            if i == 1:
                suf = new_arr[0]
                print(f"variable suf: {suf}")
                suffix.append(suf)
                print(f"suffix array at 1st append {suffix}")
            if i >= 2:
                suf = suf * new_arr[i - 1]
                print(f"variable suf: {suf}")
                suffix.append(suf)
                print(f"suffix array at nth append {suffix}")
        suffix = suffix[::-1]
        ret = []
        for i in range(len(prefix)):
            ret.append(prefix[i] * suffix[i])

        return ret