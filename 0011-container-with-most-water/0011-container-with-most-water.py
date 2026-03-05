class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        area = float('-inf')
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            curArea = h * w
            area = max(curArea, area)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return area
                

