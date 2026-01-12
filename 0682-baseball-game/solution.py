class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []

        for x in range(len(operations)):
            c = 0
            try:
                num = int(operations[x])  
                record.append(num)
                c+=1
            except ValueError:
                pass 
            if operations[x] == "+":
                record.append(record[c-1] + record[c-2])
                c+=1
            elif operations[x] == "C":
                record.remove(record[c-1])
                c-=1
            elif operations[x] == "D":
                record.append(2*(record[c-1]))
                c+=1
        return sum(record)   
