class Solution:
    def maxCoins(self, piles: List[int]) -> int:
            piles.sort()
            i = 0
            j = len(piles)-2
            res = 0
            while j > i:
                res += piles[j]
                j -= 2
                i += 1
            return res

