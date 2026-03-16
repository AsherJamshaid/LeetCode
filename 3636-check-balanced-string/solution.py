class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        odd = 0
        even = 0
        arr = list(map(int, num))
        for x in range(len(arr)):
            if x % 2 == 0:
                even+=arr[x]
            elif x % 2 != 0:
                odd+=arr[x]
        return odd == even
