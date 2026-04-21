class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = self.findStart(nums,target)
        j = self.findEnd(nums, target)
        return [i, j]
    
    def findStart(self, nums, target):
        s = 0 
        e = len(nums)-1
        low = -1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                low = m
                e = m - 1
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        
        return low

    def findEnd(self, nums, target):
        s = 0 
        e = len(nums)-1
        high = -1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                high = m
                s = m + 1
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        
        return high

            
