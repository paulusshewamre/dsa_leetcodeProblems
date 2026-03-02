class Solution:
    def frequencySort(self, s: str) -> str:
        mp = Counter(s)
        
        res = []
        sortedmp = mp.most_common()


        i = 0
        for char, count  in sortedmp:
            res.append(char*count)

        
        return "".join(res)
            

