class Solution(object):
    def findValidElements(self, nums):
        new = []
        for x in range(len(nums)):
            if x == 0 or x == len(nums) - 1:
                new.append(nums[x])
                continue
            
            greater_than_left = all(nums[x] > nums[z] for z in range(x))
            
            greater_than_right = all(nums[x] > nums[y] for y in range(x + 1, len(nums)))
            
            if greater_than_left or greater_than_right:
                new.append(nums[x])
        
        return new
