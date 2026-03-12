class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        hashing = {}

        for x in range(len(arr)):
            if arr[x] in hashing:
                hashing[arr[x]]+=1
            else:
                hashing[arr[x]] = 1
        count = 0
        for x in arr:   
            if hashing[x] == 1:
                count += 1
                if count == k:
                    return x
        
        return ""
