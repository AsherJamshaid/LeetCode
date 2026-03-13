class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        l = 0
        r = k - 1
        avg = 0
        temp = 0
        ans = 0
        for x in range(l,r+1):
            temp+=arr[x]
        avg = temp // k
        if avg >= threshold:
            ans+=1
        while r < len(arr) - 1:
            temp-=arr[l]
            l+=1
            r+=1
            temp+=arr[r]
            avg = temp // k
            if avg >= threshold:
                ans+=1
        return ans
