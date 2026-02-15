class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(0-target[0]) + abs(0-target[1])

        for i in range(len(ghosts)):
            ghost_distance = abs(ghosts[i][0]-target[0]) + abs(ghosts[i][1]-target[1])
            if ghost_distance <= distance:
                return False

        return True
