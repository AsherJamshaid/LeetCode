class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count5 = 0
        count10 = 0
        count20 = 0

        for x in range(len(bills)):
            if bills[x] == 5:
                count5+=1
            elif bills[x] == 10:
                count10+=1
                if count5 == 0:
                    return False
                count5-=1
            elif bills[x] == 20:
                count20+=1
                if (count5 >= 3) or (count5 >= 1 and count10 >= 1):
                    if(count5 >= 1 and count10 >= 1):
                        count5-=1
                        count10-=1
                    else:
                        count5-=3
                else:
                    return False
        return True
