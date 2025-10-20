class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        length = len(operations)
        for i in range(length):
            if operations[i] == "++X" or operations[i] == "X++":
                X = X + 1
            elif operations[i] == "--X" or operations[i] == "X--":
                X = X - 1
        return X

