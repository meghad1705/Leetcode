# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l=0
        c=head
        while c:
            l+=1
            c=c.next
        if l==n:
            return head.next
        c1=head
        for _ in range(l-n-1):
            c1=c1.next
        c1.next=c1.next.next
        return head