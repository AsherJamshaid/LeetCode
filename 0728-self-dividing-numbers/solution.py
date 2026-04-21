class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        result = []

        for num in range(left, right + 1):
            temp = num
            ok = True

            while temp > 0:
                digit = temp % 10

                if digit == 0:
                    ok = False
                    break

                if num % digit != 0:
                    ok = False
                    break

                temp //= 10

            if ok:
                result.append(num)

        return result


