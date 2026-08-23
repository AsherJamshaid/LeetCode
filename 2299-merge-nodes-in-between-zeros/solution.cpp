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
    ListNode* mergeNodes(ListNode* head) {

        // current = where we are reading the original list
        ListNode* current = head->next;

        // sum = sum of numbers between two 0s
        int sum = 0;

        // These will build our NEW linked list
        ListNode* newHead = NULL;
        ListNode* tail = NULL;

        while (current != NULL) {

            // We reached a 0
            if (current->val == 0) {

                // Create a new node containing the sum
                ListNode* newNode = new ListNode(sum);

                // If this is the first node
                if (newHead == NULL) {
                    newHead = newNode;
                    tail = newNode;
                }

                // Otherwise attach it after the last node
                else {
                    tail->next = newNode;
                    tail = newNode;
                }

                // Start calculating the next group
                sum = 0;
            }

            // Current node is a normal number
            else {
                sum += current->val;
            }

            // Move to the next node
            current = current->next;
        }

        return newHead;
    }
};
