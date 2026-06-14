class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in numbers:            
            print(f"n: {n}")
            compliment = target - n
            print(f"compliment: {compliment}")
            if (compliment in numbers) and (compliment < n):
                return [numbers.index(compliment) + 1, numbers.index(n) + 1]
            elif (compliment in numbers) and (compliment > n):
                return [numbers.index(n) + 1, numbers.index(compliment) + 1]
            
        return []