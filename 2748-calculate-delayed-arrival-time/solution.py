class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        temp = arrivalTime + delayedTime
        if temp >= 24:
            return temp - 24
        return temp
