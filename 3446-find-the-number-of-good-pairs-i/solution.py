class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for x in range(len(nums1)):
            for y in range(len(nums2)):
                if nums1[x] % (nums2[y] * k) == 0:
                    count +=1
        return count
