class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for x in range(len(patterns)):
            strin = patterns[x]
            if strin in word:
                count+=1
        return count
