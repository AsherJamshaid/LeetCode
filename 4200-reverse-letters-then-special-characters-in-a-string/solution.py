class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        specials = []

        for ch in s:
            if 'a' <= ch <= 'z':
                letters.append(ch)
            else:
                specials.append(ch)

        letters.reverse()
        specials.reverse()

        result = []
        i = j = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(letters[i])
                i += 1
            else:
                result.append(specials[j])
                j += 1

        return "".join(result)
