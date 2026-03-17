class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res = []
        for x in range(len(prices)):
            flag = False
            for y in range(x+1,len(prices)):
                if prices[x] >= prices[y]:
                    res.append(prices[x]-prices[y])
                    flag = True
                    break
            if flag == False:
                res.append(prices[x])
        return res
