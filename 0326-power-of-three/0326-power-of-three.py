class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.power(n)
    
    def power(self, n):
        if n == 1:
            return True
        
        elif n % 3 == 0 and n != 0:
            n /= 3
            return self.power(n)
        return False