class Solution {
public:
    int trap(vector<int>& height) {
        vector<pair<int, int>> max_left_right(height.size(), {0, 0});
        int max_left = 0;
        int max_right = 0;
        int water = 0;

        for (int i = 0; i < height.size(); i++) {
            int j = height.size() - 1 - i;

            max_left_right[i].first = max_left;
            max_left = max(max_left, height[i]);

            max_left_right[j].second = max_right;
            max_right = max(max_right, height[j]);
        }

        for (int i = 0; i < height.size(); i++) {
            auto& [left, right] = max_left_right[i];
            int minimum = min(left, right); 
            if (minimum > height[i]) {
                water += minimum - height[i];
                //cout << "+";
            }

            //cout << minimum << ",";
        }

        return water;
    }
};