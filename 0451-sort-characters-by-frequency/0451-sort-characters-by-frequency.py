class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1
        
        arr = [0] * len(s)
        sortedmpArray= sorted(mp.items(), key=lambda item:item[1], reverse=True)

        i = 0
        for key, val in sortedmpArray:
            while val > 0:
                arr[i] = key
                i+=1
                val-=1
        
        return "".join(arr)
            

