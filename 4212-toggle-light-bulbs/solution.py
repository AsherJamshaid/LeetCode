class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        result = []
        new = set(bulbs)
        new2 = list(new)
        for x in range(len(new2)):
            count = bulbs.count((new2[x]))
            if count % 2 != 0:
                result.append(new2[x])
        result.sort()
        return result
