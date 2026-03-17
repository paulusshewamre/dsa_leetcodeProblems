class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        vowels = ['a', 'e','i','o','u']
        vCnt= 0
        res = 0
        for r in range(len(s)):
            if s[r] in vowels:
                vCnt += 1

            if r-l+1 > k:
                if s[l] in vowels:
                    vCnt -= 1
                l+=1
            
            res = max(res, vCnt)
        return res

            
            

            

