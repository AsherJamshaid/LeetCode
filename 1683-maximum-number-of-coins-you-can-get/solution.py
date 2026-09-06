class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        ans = 0
        i = 1
        for x in range(len(piles)//3):
            ans+=piles[i]
            i+=2
        return ans
