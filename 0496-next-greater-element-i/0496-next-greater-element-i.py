class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            flag = False
            for m in nums2:
                if n == m:
                    flag = True
                if flag and m > n:
                    res[i] = m
                    break
        return res
            
                    

