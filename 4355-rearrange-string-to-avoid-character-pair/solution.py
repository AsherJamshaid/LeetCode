class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        res = ""
        if x not in s or y not in s:
            return s
        if x > y :
            return ''.join(sorted(s))
        return ''.join(sorted(s, reverse=True))

