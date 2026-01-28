class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        minCount = len(nums) // 3
        res = []
        for num in counter:
            if counter[num] > minCount:
                res.append(num)
        
        return res

