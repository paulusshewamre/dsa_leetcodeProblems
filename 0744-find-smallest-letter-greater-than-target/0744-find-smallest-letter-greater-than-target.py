class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = self.bs(letters, target)
        return letters[i]

    def bs(self, letters, target):
        s = 0
        e = len(letters)-1
        while s <= e:
            m = (s + e) // 2
            if letters[m] <= target:
                s = m + 1
            else:
                e = m - 1
        return s % len(letters)