from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        
        sorted_chars = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        res = ""
        for char in sorted_chars:
            res += char * count[char]
        
        return res
