class Solution:
    def scoreDifference(self, nums):
        first = 0
        second = 0
        
        active = 0  # 0 = first player, 1 = second player
        
        for i in range(len(nums)):
            
            # Rule 1: if odd → swap
            if nums[i] % 2 == 1:
                active ^= 1
            
            # Rule 2: every 6th game → swap
            if i % 6 == 5:
                active ^= 1
            
            # Give points
            if active == 0:
                first += nums[i]
            else:
                second += nums[i]
        
        return first - second
