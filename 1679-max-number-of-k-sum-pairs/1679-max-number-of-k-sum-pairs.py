class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l , r = 0 , len(nums)-1
        count = 0
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum == k:
                count += 1
                l+=1
                r-=1
            elif curSum > k:
                r-=1
            else:
                l+=1
        return count