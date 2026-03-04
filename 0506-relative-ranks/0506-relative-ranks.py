class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score)
        n = len(score)
        res = []
        for num in score:
            numIndex = sortedScore.index(num)
            rank = n - numIndex
            if rank <= 3:
                if rank == 1:
                    res.append("Gold Medal")
                elif rank == 2:
                    res.append("Silver Medal")
                else:
                    res.append("Bronze Medal")
            else:
                res.append(str(rank))
        return res



