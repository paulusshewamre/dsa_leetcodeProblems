class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = set()
        curr_sum = 0
        max_sum = 0
        l = 0

        for r in range(len(nums)):
            # Slide the window: remove duplicates
            while nums[r] in counter:
                counter.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            # Add current number
            counter.add(nums[r])
            curr_sum += nums[r]

            # Check if window size is k
            if r - l + 1 == k:
                max_sum = max(max_sum, curr_sum)
                # Slide window forward
                counter.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

        return max_sum