class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 1
        for i in range(1, len(chars)+1):
            if i == len(chars) or chars[i] != chars[i-1]:
                if count == 1:
                    s += chars[i-1]
                else:
                    s += chars[i-1]
                    s += str(count)
                count = 1
            else:
                count += 1
        
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
        
        
