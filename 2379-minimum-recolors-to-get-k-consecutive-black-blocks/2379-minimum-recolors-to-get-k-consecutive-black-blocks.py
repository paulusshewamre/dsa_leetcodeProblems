class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        res = float('inf')
        countW= 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                countW += 1
            
            if r - l + 1 == k:
                res = min(res, countW)
            
                if blocks[l] == "W":
                    countW -= 1
                
                l+=1
        return res
