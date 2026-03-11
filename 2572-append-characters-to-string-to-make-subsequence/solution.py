class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_ptr = 0
        t_ptr = 0
        ans = 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr+=1
                t_ptr+=1
            else:
                s_ptr+=1
        return len(t) - t_ptr
