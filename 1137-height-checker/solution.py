class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = []
        count = 0
        sorted_list=[]
        for x in range(len(heights)):
            expected.append(heights[x])
        sorted_list = sorted(expected)
        for x in range(len(heights)):
            if heights[x] != sorted_list[x]:
                count = count + 1
        return count
