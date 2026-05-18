class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map; // key(num) -> value(index)

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            auto it = map.find(complement);
            
            if (it != map.end()) {
                return {i, it->second};
            } else {
                map[nums[i]] = i;
            }
        }
        return {};
    }
};