class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        counter = {}
        for i in range(len(list1)):
            if list1[i] in common:
                counter[list1[i]] = counter.get(list1[i], 0) + i
        
        for i in range(len(list2)):
            if list2[i] in common:
                counter[list2[i]] = counter.get(list2[i], 0) + i
        
        res = []
        sorted_items = sorted(counter.items(), key=lambda item:item[1])
        minn = sorted_items[0][1]
        for key, value in sorted_items:
            if value <= minn:
                res.append(key)
        
        return res
