# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        s = 1
        e = n
        bad = 0
        while s <= e:
            m = (s + e) // 2
            if isBadVersion(m):
                bad = m
                e = m - 1
            else:
                s = m + 1
        
        return bad