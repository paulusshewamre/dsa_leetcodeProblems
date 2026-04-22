class Solution:
    def search(self, nums, target):
        peak_index = self.binary_search_to_find_peak(nums)
        
        if peak_index > -1 and nums[peak_index] == target:
            return peak_index
        
        ans1 = self.binary_search(nums, target, 0, peak_index)
        ans2 = self.binary_search(nums, target, peak_index + 1, len(nums) - 1)
        
        return max(ans1, ans2)

    def binary_search_to_find_peak(self, nums):
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid - 1
            
            if nums[start] >= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1

    def binary_search(self, nums, target, start, end):
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        
        return -1