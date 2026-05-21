class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); i++) {
            int complement = target - numbers[i];
            int l = i + 1;
            int r = numbers.size() - 1;
            while (r >= l) {
                int mid = l + (r - l) / 2;
                if (numbers[mid] < complement) {
                    l = mid + 1;
                } else if (numbers[mid] > complement) {
                    r = mid - 1;
                } else {
                    return {i + 1, mid + 1};
                }
            }
        }

        return {};
    }
};