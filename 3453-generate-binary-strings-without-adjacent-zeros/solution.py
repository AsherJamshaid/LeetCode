class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def generate(s, prev):
            if len(s) == n:
                result.append(s)
                return
            
            generate(s + '1' , '1')

            if prev != '0':
                generate(s + '0', '0')
        
        generate("", "")
        return result
