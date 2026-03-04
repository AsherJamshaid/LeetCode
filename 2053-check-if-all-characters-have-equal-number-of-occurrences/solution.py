class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first_count = s.count(s[0])
        flag = False
        for x in range(1,len(s)):
            if s.count(s[x]) != first_count:
                flag = True
                break
        if not flag:
            return True
        else:
            return False
