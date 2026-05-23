class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        while (true) {
            if (nums[0] == nums[nums[0]]) {
                break;
            } else {
                int temp = nums[0];
                nums[0] = nums[nums[0]];
                nums[temp] = temp;
            }
        }

        return nums[0];
    }
};