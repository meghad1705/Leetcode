# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self,head):
        p=None
        c=head
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        head=p
        return p