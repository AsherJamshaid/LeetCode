class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
    
    
        if len(pattern) != len(words):
            return False
        
        dic = {}
        
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            
            if letter in dic:
                if dic[letter] != word:
                    return False
            else:
                if word in dic.values():
                    return False
                dic[letter] = word
        
        return True
