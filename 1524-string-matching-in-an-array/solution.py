class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for x in range(len(words)):

            for y in range(len(words)):
                if words[x] == words[y]:
                    continue
                elif words[x] in words[y]:
                    result.append(words[x])
                    break
        return result
