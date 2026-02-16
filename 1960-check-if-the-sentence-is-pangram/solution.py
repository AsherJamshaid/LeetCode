class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        new = set(sentence)
        new2 = list(new)

        if len(new2) >= 26:
            return True
        else:
            return False
