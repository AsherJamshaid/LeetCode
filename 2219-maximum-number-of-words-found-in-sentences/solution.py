class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        string = ""
        max = 0
        for x in range(len(sentences)):
            string = sentences[x]
            count = 1
            for y in range(len(string)):
                if string[y] == " ":
                    count = count + 1
            if count > max:
                max = count
        return max
