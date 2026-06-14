class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        i = len(heights) - 1
        max_area = 0
        while i > j:
            curr = min(heights[j], heights[i]) * (i - j)
            if max_area < curr:
                max_area = curr
            if (heights[i] < heights[j]):
                i -= 1
            elif heights[i] > heights[j]:
                j += 1
            else:
                i -= 1
                j+=1
            
        return max_area
