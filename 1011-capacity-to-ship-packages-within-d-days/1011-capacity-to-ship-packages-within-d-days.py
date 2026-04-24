class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = low

        def limit(cap):
            days_used = 1
            curW = 0
            for w in weights:
                if w + curW > cap:
                    days_used += 1
                    curW = 0
                curW += w
            return days_used <= days

        while low <= high:
            cap = (low + high) // 2
            if limit(cap):
                ans = cap
                high = cap - 1
            else:
                low = cap + 1
        
        return ans



    