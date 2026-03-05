class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        bar_count = 0
        star = 0
        if "*" not in s:
            return 0
        elif "|" not in s:
            return s.count("*")
        else:
            for x in range(len(s)):
                if s[x] == "|":
                    bar_count+=1

                elif bar_count % 2 == 0:
                    if s[x] == "*":
                        star+=1
            return star
