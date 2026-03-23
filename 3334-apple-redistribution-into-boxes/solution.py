class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        temp = sum(apple)
        capacity.sort()
        ops = 0
        temp2 = 0
        for x in range(len(capacity)-1,-1,-1):
            temp2+=capacity[x]
            ops+=1
            if temp2 >= temp:
                break
        return ops
