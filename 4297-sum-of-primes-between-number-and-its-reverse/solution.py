class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """

        rev = int(str(n)[::-1])

        start = min(n, rev)
        end = max(n, rev)

        res = 0

        for x in range(start, end + 1):

            if x < 2:
                continue

            is_prime = True

            for j in range(2, int(x ** 0.5) + 1):
                if x % j == 0:
                    is_prime = False
                    break

            if is_prime:
                res += x

        return res
