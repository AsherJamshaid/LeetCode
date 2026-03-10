class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        cur_time = 0
        total_wait = 0
        
        for arrival, prep_time in customers:
            if arrival >= cur_time:
                # Chef free, customer doesn't wait
                start_time = arrival
            else:
                # Chef busy, customer waits
                start_time = cur_time
            
            finish_time = start_time + prep_time
            total_wait += finish_time - arrival
            cur_time = finish_time
        
        return total_wait / float(len(customers))
