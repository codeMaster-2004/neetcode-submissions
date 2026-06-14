class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = len(numbers) - 1

        while (l != n//2) or (r != n//2):
            print(f"l is {l} r is {r}")
            if numbers[l] + numbers[r] < target:
                l += 1
                print(f"l after update is {l} r is {r} ")
            elif numbers[l] + numbers[r] > target:
                r -= 1
                print(f"l is {l} r after update is {r}")
            else:
                return [l+1, r+1]