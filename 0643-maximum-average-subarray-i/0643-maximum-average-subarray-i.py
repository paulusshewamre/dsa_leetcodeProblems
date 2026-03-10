class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_sum = total / k

        for end in range(k, len(nums)):
            total += nums[end]
            total -= nums[end-k]
            max_sum = max(total/k, max_sum)
        return max_sum