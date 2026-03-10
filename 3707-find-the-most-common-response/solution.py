class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        hashing = {}

        for x in range(len(responses)):
            responses[x] = list(set(responses[x]))
            for y in range(len(responses[x])):
                response = responses[x][y]
                if response in hashing:
                    hashing[response]+=1
                else:
                    hashing[response] = 1
        max_freq = -1
        val = ""
        for key,f in hashing.items():
            if f > max_freq:
                max_freq = f
                val = key
            elif f == max_freq:              
                val = min(val, key)
        return val
