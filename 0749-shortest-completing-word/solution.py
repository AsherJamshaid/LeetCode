class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        
        new = ""
        for x in range(len(licensePlate)):
            temp = ord(licensePlate[x])
            if temp == 32 or (temp >= 48 and temp <= 57):
                continue
            else:
                new += licensePlate[x].lower()
        
        res = ""
        
        for y in range(len(words)):   
            temp2 = words[y].lower()  
            
            valid = True
            
            for x in range(len(new)):
                if temp2.count(new[x]) < new.count(new[x]):
                    valid = False
                    break
            
            if valid:
                if res == "" or len(temp2) < len(res):
                    res = temp2
        
        return res
