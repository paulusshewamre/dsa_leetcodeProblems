class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1

        while s < e:
            m = (s + e) // 2
            if nums[m] > nums[m+1]:
                e = m
            else:
                s = m + 1
        return s