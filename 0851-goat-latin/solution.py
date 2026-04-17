class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        res = ""
        vow = "aeiou"
        vow2 = "AEIOU"
        i=1
        arr = sentence.split()
        for x in range(len(arr)):
            temp = arr[x]
            if temp[0] in vow or temp[0] in vow2:
                res+=temp+"ma"
            else:
                new = temp[1::]
                new+=temp[0]+"ma"
                res+=new
            for y in range(i):
                res+="a"
            i+=1
            if x != len(arr)-1:
                res+=" "
        return res
