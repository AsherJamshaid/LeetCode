class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int(''.join(map(str, digits)))
        number+=1
        return list(map(int,str(number)))
