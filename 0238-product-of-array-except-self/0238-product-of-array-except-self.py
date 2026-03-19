class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * N 
        postfix = [1] * N
        res = [1] * N

        for i in range(1, N):
            prefix[i] = prefix[i-1] * nums[i-1]

        
        for i in range(N-2,-1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(N):
            res[i] = prefix[i] * postfix[i]
        
        print(prefix)
        print(postfix)
        return res
        

        
