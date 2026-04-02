class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        return min(abs(30.0 * hour - 11.0 / 2.0 * minutes), 360.0 - abs(30.0 * hour - 11.0 / 2.0 * minutes))
