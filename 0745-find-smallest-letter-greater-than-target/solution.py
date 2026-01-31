class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for x in range(len(letters)):
            if letters[x] > target:
                value = letters[x]
                break
            elif x == len(letters) - 1:
                value = letters[0]
                break
        return value
