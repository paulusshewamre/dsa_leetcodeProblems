class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in nums:
            res[i] = nums[nums[i]]
        return res