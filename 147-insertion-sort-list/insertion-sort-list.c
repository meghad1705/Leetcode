/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertionSortList(struct ListNode* head) {
    if (!head) return NULL;

    struct ListNode dummy;
    dummy.next = NULL;

    struct ListNode* current = head;

    while (current != NULL) {
        struct ListNode* prev = &dummy;
        
        // Find correct position
        while (prev->next != NULL && prev->next->val < current->val) {
            prev = prev->next;
        }

        // Save next node
        struct ListNode* nextNode = current->next;

        // Insert current between prev and prev->next
        current->next = prev->next;
        prev->next = current;

        // Move to next node
        current = nextNode;
    }

    return dummy.next;
}
