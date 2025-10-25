class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = s.lower()
        test = ""
        new2 = new
        for x in range(len(s)):
            if 'a' <= new2[x] <= 'z' or '0'<= new2[x] <= '9':
                test = test + new2[x]
        new3 = str(test[::-1])

        if test == new3:
            return True
        else:
            return False
        
