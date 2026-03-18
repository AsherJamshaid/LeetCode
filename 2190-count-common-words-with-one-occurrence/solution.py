class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        res = 0
        for x in range(len(words1)):
            if words1.count(words1[x]) == 1 and words2.count(words1[x]) == 1:
                res+=1
        return res
