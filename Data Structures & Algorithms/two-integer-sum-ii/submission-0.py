class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i, n in enumerate(numbers):
            comp = target - n
            for j in range (i, len(numbers)):
                if numbers[j] == comp:
                    return [i + 1, j + 1]
                else:
                    continue
        return []
                
            