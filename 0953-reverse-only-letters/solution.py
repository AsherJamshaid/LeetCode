class Solution(object):
    def reverseOnlyLetters(self, s):
        left = 0
        right = len(s) - 1
        new = list(s)

        while left < right:
            if not new[left].isalpha():
                left += 1
            elif not new[right].isalpha():
                right -= 1
            else:
                # swap letters
                new[left], new[right] = new[right], new[left]
                left += 1
                right -= 1

        return ''.join(new)
