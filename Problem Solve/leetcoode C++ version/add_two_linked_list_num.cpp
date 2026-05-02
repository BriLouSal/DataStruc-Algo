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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        // First we convert Listnodes into an Vector

        std::vector<int> v1, v2;

        ListNode* curr = l1;
        while(curr){
            // Pushbacl
            v1.push_back(curr->val);
            curr = curr->next;
        }
        curr = l2;
        while(curr){
            // Pushbacl
            v2.push_back(curr->val);
            curr = curr->next;
        }

        // Create an empty vector


        std::vector<int> result;
        int i = 0,  j = 0, carry = 0;
        // Use pointers such as that we let Node* current = head;
        while (i < v1.size() || j < v2.size() || carry) {
            int sum = carry;
            // Calculate the sum
            if(i < v1.size()) sum += v1[i++];
            if (j < v2.size()) sum += v2[j++];
            // Floor divide sum
            result.push_back(sum % 10);
            carry = sum /10;
 

        }
        // Then convert it back to ListNode

        ListNode* dummy = new ListNode(0);
        ListNode* temp = dummy;
        for(int digit: result){
            temp->next = new ListNode(digit);
            temp = temp->next;
        }

        return dummy->next;
        
    }

};