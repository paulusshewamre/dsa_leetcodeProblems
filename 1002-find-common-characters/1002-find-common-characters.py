class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        res = []

        common_count = collections.Counter(words[0])

        for i in range(1, words_size):
            curr_count = collections.Counter(words[i])

            for c in common_count.keys():
                common_count[c] = min(
                    common_count[c],
                    curr_count[c],
                )

        for c, count in common_count.items():
            for _ in range(count):
                res.append(c)
        
        return res