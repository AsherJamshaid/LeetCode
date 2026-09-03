# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arr = []

        current = head

        while current:
            arr.append(current.val)
            current = current.next

        maximum = 0
        n = len(arr)

        for i in range(n // 2):
            tot = arr[i] + arr[n - 1 - i]
            maximum = max(maximum, tot)

        return maximum
