class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum < 0) {
                    l++;
                } else if (sum > 0) {
                    r--;
                } else {
                    result.push_back({nums[i], nums[l], nums[r]});
                    //cout << nums[i] << "    " << nums[l] << "    " << nums[r] << endl;
                    l++;
                    while (nums[l - 1] == nums[l] && l < r) {
                        l++;
                    }

                    r--;
                    // while (nums[r + 1] == nums[r] && l < r) {
                    //     r--;
                    // }
                }
            }
        }

        return result;
    }
};