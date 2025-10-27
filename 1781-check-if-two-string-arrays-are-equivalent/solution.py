class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        new1 = ""
        new2 = ""

        for x in range(len(word1)):
            new1 = new1 + word1[x]
        for x in range(len(word2)):
            new2 = new2 + word2[x]            
        if new1 == new2:
            return True
        else:
            return False
