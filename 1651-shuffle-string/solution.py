class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        length = len(indices)
        result = [""] * length
        final = ""
        for x in range(length):
            index = indices[x]
            result[index]= s[x]

        for x in range(length):
            final = final + result[x]
        return final
