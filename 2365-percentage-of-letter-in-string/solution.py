class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        length = len(s)
        temp = s.count(letter)
        return (temp*100) // length
