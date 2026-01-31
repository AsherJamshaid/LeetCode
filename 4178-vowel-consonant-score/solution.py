class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        vowels = 0
        conso = 0
        vs = "aeiou"
        cs = "bcdfghjklmnpqrstvwxyz"
        for x in range(len(s)):
            if s[x] in vs:
                vowels+=1
            elif s[x] in cs:
                conso+=1
        if conso == 0:
            return 0
        else:
            return (int(floor(vowels/conso)))

