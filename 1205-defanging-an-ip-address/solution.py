class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ""
        length = len(address)
        for x in range(length):
            if address[x] != ".":
                result = result + address[x]
            else:
                result = result + "[.]"
        return result 
