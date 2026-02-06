class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        count = 0
        seats.sort()
        students.sort()

        for x in range(len(seats)):
            count+=abs(seats[x]-students[x])
        return count
