class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        hashing = {}

        for x in range(len(tasks)):
            if tasks[x] in hashing:
                hashing[tasks[x]]+=1
            else:
                hashing[tasks[x]] = 1
        ans = 0
        for x in hashing.values():
            if x == 3 or x == 2:
                ans+=1
            elif x == 1:
                return -1
            elif x % 3 == 0:
                ans += x / 3
            else:
                ans+=(x//3) + 1
        return ans
