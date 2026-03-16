class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = 0
        res2 = 0
        arr = []
        for x in range(len(nums1)):
          if nums1[x] in nums2:
            res+=1
        arr.append(res)
        
        for x in range(len(nums2)):
            if nums2[x] in nums1:
                res2+=1
        arr.append(res2)
        return arr
