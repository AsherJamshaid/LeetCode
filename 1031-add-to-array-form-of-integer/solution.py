class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = int(''.join(map(str, num)))
        n+=k
        return list(map(int, str(n)))
