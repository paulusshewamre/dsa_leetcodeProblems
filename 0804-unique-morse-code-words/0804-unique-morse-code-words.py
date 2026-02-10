class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        seen = {"".join(morseCode[ord(c) - ord('a')] for c in word)
                for word in words}
                
        return len(seen)