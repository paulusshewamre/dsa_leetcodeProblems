class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        res = 1
        count = 0
        
        for r in range(1, len(s)):
            if s[r] == s[r - 1]:
                count += 1
            
            while count > 1:
                if s[l] == s[l + 1]:
                    count -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res