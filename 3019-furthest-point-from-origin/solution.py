class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        res = 0

        for move in moves:
            if move == "L":
                res+=1
            elif move == "R":
                res-=1
            else:
                if moves.count("L") > moves.count("R"):
                    res+=1
                else:
                    res-=1
        return abs(res)
