class Solution(object):
    def kthCharacter(self, k):
        word = "a"
        
        while len(word) < k:
            new = ""
            for ch in word:
                new += chr(ord(ch) + 1)
            
            word += new
        
        return word[k-1]
