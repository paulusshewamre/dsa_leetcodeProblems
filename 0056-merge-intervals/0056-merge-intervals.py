class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedInterval = sorted(intervals, key=lambda x: x[0])
        res = []
        res.append(sortedInterval[0])
        cur = 0
        for i in range(1, len(intervals)):
            if sortedInterval[i][0] <= res[cur][1]:
                res[cur][1] = max(res[cur][1], sortedInterval[i][1])
            else:
                res.append(sortedInterval[i])
                cur += 1

        return res        