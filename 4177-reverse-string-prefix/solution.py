class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        string = s[:k]
        new = string[::-1]
        new+=s[k::]
        return new
