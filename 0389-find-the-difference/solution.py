class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        arr1 = [0]*26
        arr2 = [0]*26

        for x in range(len(s)):
            arr1[ord(s[x])-ord('a')]+=1
        for x in range(len(t)):
            arr2[ord(t[x])-ord('a')]+=1
        
        for x in range(26):
            if arr1[x] != arr2[x]:
                return chr(97+x)
        
