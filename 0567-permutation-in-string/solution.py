class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)

        if n1> n2:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        for x in range(n1):
            s1_count[ord(s1[x]) - ord('a')]+=1
            s2_count[ord(s2[x]) - ord('a')]+=1

        if s1_count == s2_count:
            return True
        
        for x in range(n1,n2):
            s2_count[ord(s2[x]) - 97] +=1 
            s2_count[ord(s2[x-n1]) - ord('a')] -=1
            if s1_count == s2_count:
                return True
        return False
