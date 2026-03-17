class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum += nums[i]
            nums[i] = curSum
        
        return nums