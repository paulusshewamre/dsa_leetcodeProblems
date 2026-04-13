class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for c in tokens:
            if c == "+":
                stk.append(stk.pop() + stk.pop())
            elif c == "-":
                second, first = stk.pop(), stk.pop()
                stk.append(first - second)
            elif c == "*":
                stk.append(stk.pop() * stk.pop())
            elif c == "/":
                second, first = stk.pop(), stk.pop()
                stk.append(int(first / second))                
            else:
                stk.append(int(c))
        
        return stk[0]