class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            code = ""
            for char in word:
                code += morseCode[ord(char)-97]
            res.append(code.strip())
        
        return len(set(res))