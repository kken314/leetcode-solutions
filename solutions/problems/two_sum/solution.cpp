class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            int find = target - nums[i];
            for (int j = 0; j < nums.size(); j++) {
                if (find == nums[j] && i != j) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
