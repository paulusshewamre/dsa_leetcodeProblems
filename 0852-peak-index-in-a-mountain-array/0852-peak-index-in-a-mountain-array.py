class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.bs(arr)

    def bs(self, arr):
        s = 0
        e = len(arr)-1

        while s < e:
            m = (s + e) // 2
            if arr[m] > arr[m+1]:
                e = m
            else:
                s = m + 1
        return s