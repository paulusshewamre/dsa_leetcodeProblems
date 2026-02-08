class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        counter = { word: i for i, word in enumerate(list1)}
        minSum = float('inf')
        res = []

        for j , word in enumerate(list2):
            if word in counter:
                indexSum = j + counter[word]
                if indexSum < minSum:
                    minSum = indexSum
                    res = [word]
                elif indexSum == minSum:
                    res.append(word)
        return res
