class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        new3 = []

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for x in range(len(s)):
            new3.append(freq[s[x]])

        for x in range(len(new3)):
            if new3[x] == 1:
                return x

        return -1
