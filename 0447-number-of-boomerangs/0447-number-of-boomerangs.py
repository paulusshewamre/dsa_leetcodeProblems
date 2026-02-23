class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            commonDistance = {}
            for q in points:
                x = p[0] - q[0]
                y = p[1] - q[1]
                commonDistance[x*x + y*y] = 1 + commonDistance.get(x*x + y*y, 0)
            for k in commonDistance:
                res += commonDistance[k] * (commonDistance[k] - 1)
        return res


