class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        
        count = 0
        for word in words:
            flag = False
            for ch in word:
                if ch not in allowed:
                    flag = True
                    break
            if flag == False:
                count+=1
        return count

