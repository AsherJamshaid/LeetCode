class Solution(object):
    def minimumRecolors(self, blocks, k):

        wcount = 0
        
        for i in range(k):
            if blocks[i] == "W":
                wcount += 1
        
        minops = wcount
        
        for r in range(k, len(blocks)):
            
            if blocks[r] == "W":
                wcount += 1
                
            if blocks[r-k] == "W":
                wcount -= 1
                
            minops = min(minops, wcount)
        
        return minops
