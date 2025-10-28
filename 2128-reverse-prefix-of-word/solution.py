class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        new = ""
        reverse = ""
        count = 0
        found = 0
        for x in range(len(word)):
            if word[x] == ch:
                new = new + word[x]
                found = 1
                count = count + 1
                break
            else:
                new = new + word[x]
                count = count + 1
    
        if found == 1:    
            reverse = new[::-1]
            reverse = reverse + word[count::1]
            return reverse
        else:
            return word
