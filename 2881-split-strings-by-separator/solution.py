class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        res = ""

        for x in range(len(words)):
            temp = words[x].replace(separator," ")
            res+=temp + " "
        return res.split()
