class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        hMap = {}
        for i in range(n):
            hMap[heights[i]] = names[i]
        
        heights.sort(reverse=True)
        for i in range(n):
            names[i] = hMap[heights[i]]
        
        return names

            