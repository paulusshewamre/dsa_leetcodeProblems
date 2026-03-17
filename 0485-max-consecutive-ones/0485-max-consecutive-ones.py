class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] != 1:
                count = 0
            else:
                count += 1
            i+=1
            res = max(count, res)
        
        return res

