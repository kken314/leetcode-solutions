/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        unordered_set<ListNode*> visitedA;
        unordered_set<ListNode*> visitedB;

        ListNode* currA = headA;
        ListNode* currB = headB;

        while (currA || currB) {
            if (currA) {
                if (visitedB.find(currA) != visitedB.end()) {
                    return currA;
                }
                visitedA.insert(currA);
                currA = currA->next;
            }
            if (currB) {
                if (visitedA.find(currB) != visitedA.end()) {
                    return currB;
                }
                visitedB.insert(currB);
                currB = currB->next;
            }
        }

        return nullptr;
    }
};