class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashing = {}

        for x in range(len(arr)):
            if arr[x] in hashing:
                hashing[arr[x]]+=1
            else:
                hashing[arr[x]]=1
        temp = list(hashing.values())
        if len(hashing) == len(set(temp)):
            return True
        else:
            return False
