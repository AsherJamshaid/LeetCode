class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        leftptr = 0
        rightptr = len(numbers) - 1

        for x in range(len(numbers)):
            if numbers[leftptr] + numbers[rightptr] == target:
                result.append(leftptr+1)
                result.append(rightptr+1)
                break
            elif numbers[leftptr] + numbers[rightptr] > target:
                rightptr-=1
            
            elif numbers[leftptr] + numbers[rightptr] < target:
                leftptr+=1
        return result
