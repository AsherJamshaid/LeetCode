class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        flag = True
        for x in range(len(words)):
            reverse_String = words[x][::-1]
            if reverse_String == words[x]:
                flag = False
                return(words[x])
                break

        if flag == True:
            return ""
