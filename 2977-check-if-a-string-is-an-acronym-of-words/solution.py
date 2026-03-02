class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        
        new = ""
        for x in range(len(words)):
            strin = words[x]
            new+=strin[0]
        return new == s
