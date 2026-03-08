class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        arr = []
        for x in range(len(capacity)):
            if capacity[x] >= itemSize:
                arr.append(capacity[x])
        if len(arr) >= 1:
            return capacity.index(min(arr))
        else:
            return -1
