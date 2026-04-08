class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i].isalnum():
                stk.append(s[i])
            elif s[i] == "*":
                stk.pop()
        return "".join(stk)