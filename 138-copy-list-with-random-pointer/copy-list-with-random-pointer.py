"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        
        if not head:
            return None
        c=head
        while c:
            new = Node(c.val)
            new.next =  c.next
            c.next = new
            c = c.next.next
        c=head
        while c:
            if c.random:
                c.next.random = c.random.next
            c=c.next.next
        #create head for  clone
        clone_head = head.next
        # create current pointers for original and clone
        c=head
        c1=clone_head
        while c:
            c.next=c.next.next
            if c1.next:
                c1.next=c1.next.next
            c=c.next
            c1=c1.next
        return clone_head