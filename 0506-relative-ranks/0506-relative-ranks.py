class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sCopy = score.copy()
        mp = defaultdict(int)

        for i in range(n):
            mp[sCopy[i]] = i
        
        sCopy.sort(reverse=True)

        rank = [""] * n
        for i in range(n):
            if i == 0:
                rank[mp[sCopy[i]]] = "Gold Medal"
            elif i == 1:
                rank[mp[sCopy[i]]] = "Silver Medal"
            elif i == 2:
                rank[mp[sCopy[i]]] = "Bronze Medal"
            else:
                rank[mp[sCopy[i]]] = str(i+1)
        return rank




