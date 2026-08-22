/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* previous = NULL;
        ListNode* current = head;
        while(current != NULL){
            if(current->val == val){
                    if(current == head){
                        head = current->next;
                        current = current->next;
                    }
                    else{
                        previous->next = current->next;
                        current = current->next;
                    }
            }
            else{
                previous = current;
                current = current->next;
            }
        }
        return head;
    }
};
