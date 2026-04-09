class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stk = []

        for num in reversed(nums2):
            while stk and stk[-1] <= num:
                stk.pop()
            
            mp[num] = -1 if not stk else stk[-1]
            stk.append(num)
        
        return [mp[num] for num in nums1]
                    

