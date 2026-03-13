class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal > 0:
            subArray1 = self.helper(nums, goal)
            subArray2 = self.helper(nums, goal - 1)
            return subArray1 - subArray2
        return self.helper(nums, goal)

    def helper(self, nums, goal):
        l, r = 0, 0
        s = 0
        cnt = 0

        while r < len(nums):
            s += nums[r]

            while l <= r and s > goal:
                s -= nums[l]
                l += 1

            cnt += r - l + 1
            r += 1

        return cnt