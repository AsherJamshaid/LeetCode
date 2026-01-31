class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        if len(word1) == len(word2):
            for x in range(len(word1)):
                result+=word1[x] + word2[x]
        elif len(word1) < len(word2):
            for x in range(len(word1)):
                result+=word1[x] + word2[x]
            result+=word2[len(word1):]
        else:
            for x in range(len(word2)):
                result+=word1[x] + word2[x]
            result+=word1[len(word2):]
        return result
