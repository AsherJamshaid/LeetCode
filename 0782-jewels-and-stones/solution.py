class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for x in range(len(stones)):
            for y in range(len(jewels)):
                if stones[x] == jewels[y]:
                    count = count + 1
        return count
        
