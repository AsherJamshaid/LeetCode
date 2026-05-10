class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        res = []
        score = 0
        counter = 0
        for x in range(len(events)):
            if counter == 10:
                break
            elif events[x] == "W":
                counter+=1
            elif events[x] == "WD":
                score+=1
            elif events[x] == "NB":
                score+=1
            else:
                score+=int(events[x])
        res.append(score)
        res.append(counter)
        return res
