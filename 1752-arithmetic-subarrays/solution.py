class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        res = []
        for x in range(len(l)):
            temp = []
            
            temp = nums[l[x]:r[x]+1]
            if len(temp) < 2:
                res.append(False)
                continue
            flag = True
            temp.sort()
            for z in range(len(temp)-1):
                if (temp[z+1] - temp[z]) != (temp[1] - temp[0]):
                    flag = False
                    break
            if flag:
                res.append(True)

            else:
                res.append(False)
        
        return res
