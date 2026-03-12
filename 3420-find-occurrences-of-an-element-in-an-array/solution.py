class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        temp = []
        res = []
        for i in range(len(nums)):
            if nums[i] == x:
                temp.append(i)
        for j in range(len(queries)):
            if len(temp) < queries[j]:
                res.append(-1)
            else:
                res.append(temp[queries[j]-1])

        return res
