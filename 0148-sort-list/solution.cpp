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
    ListNode* merge(ListNode* a, ListNode* b) {
        ListNode* head = nullptr;
        if (a->val <= b->val) {
            head = a;
            a = a->next;
        } else {
            head = b;
            b = b->next;
        }
        ListNode* curr = head;
        while (a && b) {
            if (a->val <= b->val) {
                curr->next = a;
                a = a->next;
                curr = curr->next;
            } else {
                curr->next = b;
                b = b->next;
                curr = curr->next;
            }
        }
        if (a) curr->next = a;
        if (b) curr->next = b;
        return head;
    }

    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* mid = slow->next;
        slow->next = nullptr;
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);
        return merge(left, right);
    }
};
