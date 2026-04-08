class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for s in logs:
            if s== '../':
                if len(stk) > 0:
                    stk.pop()
            elif s == "./":
                continue
            else:
                stk.append(1)
        
        return len(stk)