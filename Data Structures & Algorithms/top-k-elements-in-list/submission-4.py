class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            print(f"the dict while loading is: {count}")
            count[n] = 1 + count.get(n, 0)
        print(f"dict is: {count}")

        freq = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)
        print(f"array is: {freq}")

        ret = []
        for n in range(len(freq) - 1, 0, -1):
            for i in freq[n]:
                ret.append(i)
                if len(ret) == k:
                    return ret