class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        return self.binarySearch(nums, k)

    def binarySearch(self, nums, target):
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
        return low if low != -1 else s
        