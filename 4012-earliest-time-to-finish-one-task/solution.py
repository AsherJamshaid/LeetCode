class Solution:
    def earliestTime(self, tasks):
        earliest = float('inf')
        
        for i in range(len(tasks)):          
            total = 0
            for j in range(len(tasks[i])):   
                total += tasks[i][j]
            
            if total < earliest:
                earliest = total
        
        return earliest
