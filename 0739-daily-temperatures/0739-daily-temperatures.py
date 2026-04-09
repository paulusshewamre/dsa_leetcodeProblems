class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i, cnum in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < cnum:
                index = stk.pop()
                res[index] = i - index
            stk.append(i)
        
        return res