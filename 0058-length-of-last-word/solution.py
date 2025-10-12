class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new = s[::-1]
        x = 0
        count = 0
        for x in range((len(s))):
            if new[x] != " ":
                count = count + 1
                if x + 1 == len(new) or new[x + 1] == " ":

                    break
            else:
                continue

        return count
