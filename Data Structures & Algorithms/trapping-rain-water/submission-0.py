class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[0]
        r_max = height[r]

        water = 0

        
        while l <= r :
            if height[l] > l_max:
                l_max = height[l]
            if height[r] > r_max:
                r_max = height[r]
            
            if l_max < r_max:
                if l_max - height[l] > 0:
                    water += l_max - height[l]
                l += 1
            else:
                if r_max - height[r] > 0:
                    water += r_max - height[r]
                r -= 1
            
        return water