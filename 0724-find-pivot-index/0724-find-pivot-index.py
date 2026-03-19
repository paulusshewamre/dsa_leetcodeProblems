class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        rprefixSum = [0] * len(nums)

        acc=0
        for i in range(len(nums)):
            acc += nums[i]
            prefixSum[i] = acc
        
        acc=0

        nums.reverse()
        for i in range(len(nums)):
            acc += nums[i]
            rprefixSum[i] = acc
        
        rprefixSum.reverse()
        for i in range(len(nums)):
            if prefixSum[i] == rprefixSum[i]:
                return i
            
        return -1
