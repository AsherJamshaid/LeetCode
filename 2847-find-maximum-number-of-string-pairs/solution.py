class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                if words[x] == words[y][::-1]:
                    res+=1
        return res
