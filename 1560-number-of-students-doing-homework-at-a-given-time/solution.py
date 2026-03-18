class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        ans = 0
        for x in range(len(startTime)):
            if startTime[x] <= queryTime and endTime[x] >= queryTime:
                ans+=1
        return ans
