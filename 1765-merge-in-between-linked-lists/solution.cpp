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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode * current1 = list1;
        ListNode * current2 = list2;
        ListNode* beforeA = NULL;
        ListNode* beforeB = NULL;
        int count = 0;
        while(current1 != NULL){
            if(count == (a-1)){
                beforeA = current1;
            }
            if(count == (b+1)){
                beforeB = current1;
            }
            current1 = current1->next;
            count++;
        }
        beforeA->next = current2;
        while(current2->next != NULL) {
            current2 = current2->next;
        }
        current2->next = beforeB;
        return list1;
        
    }
};
