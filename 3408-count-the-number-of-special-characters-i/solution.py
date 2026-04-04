class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        temp = word.lower()
        new = list(set(temp))
        ans = 0
        for x in range(len(new)):
            if new[x].upper() in word and new[x].lower() in word:
                ans+=1
        return ans

