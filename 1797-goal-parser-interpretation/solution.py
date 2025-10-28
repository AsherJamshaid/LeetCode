class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        new = ""
        for x in range(len(command)):
            if command[x] == "G":
                new = new + "G"
            elif command[x] == "(" and command[x+1] == ")":
                new = new + "o"
            elif command[x] == "(" and command[x+1] == "a":
                new = new + "al"
        return new
