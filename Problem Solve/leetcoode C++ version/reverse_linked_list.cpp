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
    ListNode* reverseList(ListNode* head) {
        if(!head){
            return nullptr;
        }
        vector<int> l1;

        ListNode* curr = head;
        while(curr){
            l1.push_back(curr->val);
            curr = curr->next;
        }
        std::reverse(l1.begin(), l1.end());

        ListNode* dummy =new ListNode(l1[0]);
        ListNode* temp = dummy;
        for(int i: l1){
            temp->next = new ListNode(i);
            temp = temp->next;
        }
        return dummy->next;
    }

};