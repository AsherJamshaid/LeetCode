class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        temp = 0
        ans = 0
        for x in range(len(requests)):
            ans += abs(requests[x] - temp)
            temp = requests[x]
        return ans
