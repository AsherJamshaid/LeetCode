class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = list(map(int, str(n)))
        digit_sum = 0
        square_sum = 0
        for x in range(len(arr)):
            digit_sum += arr[x]
            square_sum += (arr[x] * arr[x])
        return square_sum - digit_sum >= 50

