class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        temp = [""] * len(arr)
        for x in range(len(arr)):
            word = arr[x][:-1]
            idx = int(arr[x][-1])
            temp[idx-1] = word
        return " ".join(temp)
