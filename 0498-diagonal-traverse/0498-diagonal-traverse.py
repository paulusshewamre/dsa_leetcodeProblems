class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        N, M = len(mat), len(mat[0])
        res, intrim = [], []

        for d in range(N+M-1):
            intrim.clear()
            r,c = 0 if d < M else d-M+1, d if d < M else M-1
            while r < N and c > -1:
                intrim.append(mat[r][c])
                r+=1
                c-=1
            if d%2 == 0:
                res.extend(intrim[::-1])
            else:
                res.extend(intrim)
        return res