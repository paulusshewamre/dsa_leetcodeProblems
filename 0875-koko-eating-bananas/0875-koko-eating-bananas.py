class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)

        def dRate(t):
            daysCount = 0

            for p in piles:
                daysCount += math.ceil(p/t)

            return daysCount

        res = e

        while s <= e:
            m = (s + e) // 2
            if dRate(m) <= h:
                res = m
                e = m - 1
            else:
                s = m + 1
        
        return res