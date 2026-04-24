# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n
        res = 0
        while s <= e:
            m = (s + e) // 2
            if guess(m) == 0:
                res = m
                return m
            elif guess(m) == 1:
                s = m + 1
            else:
                e = m - 1
        return res
        