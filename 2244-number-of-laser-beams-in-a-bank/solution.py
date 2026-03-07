class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        new = []
        for x in range(len(bank)):
            strin = bank[x]          
            if '1' not in strin:    
                continue
            else:
                new.append(strin.count('1'))  

        total = 0
        prev = 0
        for c in new:
            total += prev * c
            prev = c
        return total
