class Solution:
    def maxArea(self, height):

        start = 0
        end = len(height) - 1
        maxWater = 0

        while start < end:

            width = end - start

            if height[start] < height[end]:
                area = width * height[start]
                maxWater = max(maxWater, area)
                start += 1
            else:
                area = width * height[end]
                maxWater = max(maxWater, area)
                end -= 1

        return maxWater