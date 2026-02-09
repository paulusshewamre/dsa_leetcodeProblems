class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i+=1

        res = [] 
        for j in range(len(nums)):
            if j+1 != nums[j]:
                res.append(nums[j])

        return res