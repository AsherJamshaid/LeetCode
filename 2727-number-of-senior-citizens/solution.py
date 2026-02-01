class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0
        for x in range(len(details)):
            string = details[x]
            first = string[11]
            second = string[12]
            new = first + second
            if int(new) > 60:
                count+=1
        return count
