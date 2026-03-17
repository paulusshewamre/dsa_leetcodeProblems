class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        maxSum = 0
        curSum = 0
        unique = set()
        for r in range(len(nums)):
            while nums[r] in unique:
                unique.remove(nums[l])
                curSum-=nums[l]
                l+=1
            
            curSum += nums[r]
            maxSum = max(maxSum, curSum)
            unique.add(nums[r])
        
        return maxSum
            
            
