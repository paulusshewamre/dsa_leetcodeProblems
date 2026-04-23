class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target)
    
    def binarySearch(self, nums, target):
        s = 0
        e = len(nums)-1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        
        return s