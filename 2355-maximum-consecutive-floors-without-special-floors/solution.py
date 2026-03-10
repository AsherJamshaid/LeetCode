class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        #case1
        case_one = special[0] - bottom
        #case2
        case_two = top - special[len(special)-1]

        #case3 
        ma = -1
        for x in range(len(special)-1):
            temp = special[x+1] - special[x] - 1
            if temp > ma:
                ma = temp
        return max(case_one,case_two,ma)
