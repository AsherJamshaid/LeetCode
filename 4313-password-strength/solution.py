class Solution(object):
    def passwordStrength(self, password):
        """
        :type password: str
        :rtype: int
        """
        points = 0
        new = list(set(password))
        for x in range(len(new)):
            if ord(new[x]) >= 48 and ord(new[x]) <= 57:
                points+=3
            elif ord(new[x]) >= 65 and ord(new[x]) <= 90:
                points+=2
            elif ord(new[x]) >= 97 and ord(new[x]) <= 122:
                points+=1
            else:
                points+=5
        return points

