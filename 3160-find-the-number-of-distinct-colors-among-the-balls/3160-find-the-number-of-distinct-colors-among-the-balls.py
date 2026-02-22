class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        ball_to_color = {}
        color_count = {}

        for i, (val, color) in enumerate(queries):
            # remove old color if exists
            if val in ball_to_color:
                old = ball_to_color[val]
                color_count[old] -= 1
                if color_count[old] == 0:
                    del color_count[old]

            # assign new color
            ball_to_color[val] = color
            color_count[color] = color_count.get(color, 0) + 1

            res[i] = len(color_count)

        return res