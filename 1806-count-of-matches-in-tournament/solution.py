class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count1 = 0
        count2 = 0
        matches = 0
        adv = 0
        while n > 1:
            if n % 2 == 0:
                matches = n // 2
                adv = n - matches
                n = adv
                count1 += matches
            else:
                matches = (n - 1) // 2
                adv = (n - 1) // 2 + 1
                n = adv
                count2 += matches
            
        return (count1 + count2)


