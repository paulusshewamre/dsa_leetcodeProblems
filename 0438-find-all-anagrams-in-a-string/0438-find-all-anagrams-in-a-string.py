class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        r = len(p)-1
        p_sorted = sorted(p)
        res = []
        while r < len(s):
            word = sorted(s[l:r+1])
            if word == p_sorted:
                res.append(l)
            l+=1
            r+=1
        return res