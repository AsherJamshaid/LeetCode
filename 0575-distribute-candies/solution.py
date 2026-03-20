class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        length = len(candyType) // 2
        if length <= len(set(candyType)):
            return length
        return len(set(candyType))
