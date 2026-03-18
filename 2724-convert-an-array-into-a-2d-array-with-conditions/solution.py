class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = []  
        for x in range(len(nums)):
            placed = False
            for temp in arr:        
                if nums[x] not in temp:
                    temp.append(nums[x])
                    placed = True
                    break
            if not placed:         
                arr.append([nums[x]])

        return arr

