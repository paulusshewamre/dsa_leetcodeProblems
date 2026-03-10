class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxAvg = total / k

        for i in range(k, len(nums)):
            total -= nums[i-k]
            total += nums[i]
            localAvg = total / k
            maxAvg = max(maxAvg , localAvg)
        return maxAvg