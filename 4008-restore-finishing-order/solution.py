class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        result = []
        for x in range(len(order)):

            for y in range(len(friends)):
                if order[x] == friends[y]:
                    result.append(friends[y])
        return result
