class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                count+=1
            if count == 3:
                res = nums[i]
                break  
        return res