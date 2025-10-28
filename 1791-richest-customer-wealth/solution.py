class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for x in range(len(accounts)):
            sum = 0
            for y in range(len(accounts[x])):
                sum = sum + accounts[x][y]
                if sum > max:
                    max = sum
        return max
