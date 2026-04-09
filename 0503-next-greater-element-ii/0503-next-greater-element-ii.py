class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stk = []

        for i in range(2*n-1, -1, -1):
            cur = nums[i % n]

            while stk and stk[-1] <= cur:
                stk.pop()

            if i < n:
                res[i] = -1 if not stk else stk[-1]
            
            stk.append(cur)
        
        return res