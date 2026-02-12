class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0

        length = len(pref)
        for x in range(len(words)):
            string = words[x]
            if string[:length] == pref:
                count+=1
        return count
