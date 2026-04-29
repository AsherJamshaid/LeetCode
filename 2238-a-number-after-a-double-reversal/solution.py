class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        arr = list(str(num))
        if len(arr) == 1:

            return True
        if arr[len(arr)-1] == '0':
            return False
        return True
