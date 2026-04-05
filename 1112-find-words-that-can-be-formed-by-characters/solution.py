class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        freq = [0] * 26
        
        for ch in chars:
            freq[ord(ch) - ord('a')] += 1
        
        ans = 0
        
        for word in words:
            temp = freq[:]   
            good = True
            
            for ch in word:
                idx = ord(ch) - ord('a')
                
                if temp[idx] == 0:
                    good = False
                    break
                else:
                    temp[idx] -= 1
            
            if good:
                ans += len(word)
        
        return ans
