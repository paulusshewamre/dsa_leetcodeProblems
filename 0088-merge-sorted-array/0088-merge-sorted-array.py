class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        copyNums1 = nums1[:m]
        p1 = 0
        p2 = 0 
        r = 0 

        while p1 < m and p2 < n:
            if copyNums1[p1] <= nums2[p2]:
                nums1[r] = copyNums1[p1]
                p1+=1
            else:
                nums1[r] = nums2[p2]
                p2+=1
            r+=1
            
            
        while p1 < m:
            nums1[r] = copyNums1[p1]
            p1+=1
            r+=1

        while p2 < n:
            nums1[r] = nums2[p2]
            p2+=1
            r+=1
        
        return nums1

