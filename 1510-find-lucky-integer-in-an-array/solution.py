class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hashing = {}

        for x in range(len(arr)):
            if arr[x] in hashing:
                hashing[arr[x]] +=1
            else:
                hashing[arr[x]] = 1
        flag = False
        high_num = 0
        for n,freq in hashing.items():
            if n == freq:
                flag = True
                if n > high_num:
                    high_num = n
        if flag:
            return high_num
        else:
            return -1
