class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            h1 = 0
            for k in piles:
                h1 += math.ceil(k / m)
            if h1 > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m-1
        return res
