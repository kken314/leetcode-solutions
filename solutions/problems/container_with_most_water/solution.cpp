class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int max_val = 0;

        while (l < r) {
            int w = r - l;
            int h = min(height[l], height[r]);
            max_val = max(max_val, w * h);

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return max_val;
    }
};