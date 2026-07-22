class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        tank_area = 0
        for i in range(n - 1):
            l = i
            r = i + 1
            while r < n:
                area = min(heights[l], heights[r]) * (r - l)
                if tank_area < area:
                    tank_area = area
                else:
                    r += 1
                    continue
        return tank_area