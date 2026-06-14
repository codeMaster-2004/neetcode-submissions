class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        target = {}

        final = False
        for i in range(len(nums)):
            print("target", target)
            print("nums", nums[i])
            if nums[i] not in target:
                target[nums[i]] = 1
                print("target add", target)
                # print('target number', target[i])
            else:
                # print("target else", target[i])
                target[nums[i]] += 1
            # print(target[nums[i]])
            if (target[nums[i]] > 1):
                final = True
                break
        
        return final
