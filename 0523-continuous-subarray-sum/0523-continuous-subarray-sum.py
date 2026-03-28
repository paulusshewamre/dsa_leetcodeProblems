from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        remainder_map = {0: -1}  

        for i, num in enumerate(nums):
            prefix += num

            
            if k != 0:
                prefix %= k

            if prefix in remainder_map:
                if i - remainder_map[prefix] > 1:
                    return True
            else:
                remainder_map[prefix] = i

        return False