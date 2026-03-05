class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
        return l
            