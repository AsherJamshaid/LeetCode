class Solution(object):
    def greatestLetter(self, s):
        new = list(s)
        new.sort()
        
        for x in range(len(new)-1, -1, -1):
            if new[x].isupper():
                if new[x].lower() in new:
                    return new[x]
            else:
                if new[x].upper() in new:
                    return new[x].upper()
        return ""
