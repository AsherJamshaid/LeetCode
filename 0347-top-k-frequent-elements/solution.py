class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashing = {}
        result = []
        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]]+=1
            else:
                hashing[nums[x]] = 1
        for x in range(k):
            max_freq = -1
            max_num = None
            for num, f in hashing.items():
                if f > max_freq:
                    max_freq = f
                    max_num = num
            result.append(max_num)
            del hashing[max_num]
        return result
        
        
