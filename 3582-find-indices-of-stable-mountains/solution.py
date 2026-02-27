class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        result = []
        for x in range(1,len(height)):
            if height[x-1] > threshold:
                result.append(x)
        return result
