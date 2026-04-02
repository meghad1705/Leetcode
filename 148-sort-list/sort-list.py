class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Step 1: Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # Split the list
        
        # Step 2: Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Attach remaining nodes
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next
