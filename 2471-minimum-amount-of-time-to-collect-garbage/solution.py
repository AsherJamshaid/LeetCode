class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        mcount = -1
        gcount = -1
        pcount = -1
        total = 0
        for x in range(len(garbage)):
            total+=len(garbage[x])
            if "M" in garbage[x]:
                mcount = x
            if "P" in garbage[x]:
                pcount = x
            if "G" in garbage[x]:
                gcount = x
        travel_sum = 0
        for i in range(len(travel)):
            travel_sum += travel[i]  
            
            if i < mcount:
                total += travel[i]
            if i < pcount:
                total += travel[i]
            if i < gcount:
                total += travel[i]
        
        return total
        
