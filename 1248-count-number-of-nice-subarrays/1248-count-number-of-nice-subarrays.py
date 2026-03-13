class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if k == 0:
            return self.helper(nums, k)
        return self.helper(nums, k) - self.helper(nums, k-1)


    def helper(self, nums, k):
        l, r = 0, 0
        cnt = 0
        total = 0

        while r < len(nums):
            if nums[r] % 2 != 0:
                total += 1
            
            while l <= r and total > k:
                if nums[l] % 2 != 0:
                    total -= 1
                l+=1
            
            cnt += r - l + 1
            r+=1
        return cnt
            