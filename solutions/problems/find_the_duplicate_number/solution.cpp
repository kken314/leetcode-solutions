class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0;
        int fast = 0;

        while (true) {
            slow = nums[slow];
            fast = nums[fast];
            fast = nums[fast];
            //cout << "slow : " << slow << " fast : " << fast << endl;
            if (slow == fast) {
                break;
            }
        }

        //cout << endl << "Intercept found" << endl << endl;

        int head = 0;
        while (true) {
            slow = nums[slow];
            head = nums[head];
            //cout << "slow : " << slow << " head : " << head << endl;
            if (head == slow) {
                break;
            }
        }

        return head;
    }
};