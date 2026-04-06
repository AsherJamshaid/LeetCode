class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = []
        for x in range(len(s)):
            temp = s[x].lower()
            if temp in "aeiou":
                new.append(s[x])
        new.sort()
        ans = []
        vow = 0
        for x in range(len(s)):
            if s[x].lower() not in "aeiou":
                ans.append(s[x])
            else:
                ans.append(new[vow])
                vow+=1
        return "".join(ans)
