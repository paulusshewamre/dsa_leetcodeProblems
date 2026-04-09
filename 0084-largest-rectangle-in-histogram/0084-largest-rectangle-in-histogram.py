class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        ans = 0

        for i, height in enumerate(heights):
            start = i
            while stk and stk[-1][0] > height:
                h, j = stk.pop()
                w = i - j
                area = w * h
                ans = max(ans, area)
                start = j

            stk.append((height, start))
        
        while stk:
            h, j = stk.pop()
            w = len(heights) - j
            area = w * h
            ans = max(ans, area)

        return ans

        
