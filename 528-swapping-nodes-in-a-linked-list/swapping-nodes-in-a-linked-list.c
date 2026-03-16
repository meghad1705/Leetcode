struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode* temp = head;
    int n = 0;
    while(temp != NULL){//to find the length of list
        n++;
        temp = temp->next;
    }

    struct ListNode* first = head;
    struct ListNode* second = head;
// move first to kth node
    for(int i = 1; i < k; i++){
        first = first->next;
    }
    //move second to (n-k+1)th node
    for(int i = 1; i < n-k+1; i++){
        second = second->next;
    }
    int tempVal = first->val;
    first->val = second->val;
    second->val = tempVal;

    return head;
}
