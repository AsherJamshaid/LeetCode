class Solution(object):
    def addSpaces(self, s, spaces):
        left = 0
        right = 0
        res = []

        while left < len(s):
            if right < len(spaces) and left == spaces[right]:
                res.append(" ")
                right += 1

            res.append(s[left])
            left += 1

        return "".join(res)
