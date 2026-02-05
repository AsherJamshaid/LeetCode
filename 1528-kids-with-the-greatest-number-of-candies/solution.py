class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        count = 0
        result = []
        for x in range(len(candies)):
            count = candies[x] + extraCandies
            if count >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result 








    
