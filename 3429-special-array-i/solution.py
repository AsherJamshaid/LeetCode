class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        else:
            flag = False
            for x in range(len(nums)-1):
                first = nums[x]
                sec = nums[x+1]
                if not ((first % 2 == 0 and sec % 2 != 0) or (first % 2 != 0 and sec % 2 == 0)):
                    flag = True
            if flag == False:
                return True
            else:
                return False
