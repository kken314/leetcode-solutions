class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            //cout << "left : " << left << " mid : " << mid << " right : " << right << endl;
            //cout << "nums[left] : " << nums[left] << " nums[mid] : " << nums[mid] << " nums[right] : " << nums[right] << endl;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] >= nums[left]) { // The mid value is in the left portion
                if (nums[left] <= target && target <= nums[mid]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            } else {//(nums[mid] <= nums[right] // The mid value is in the right portion
                if (nums[mid] <= target && target <= nums[right]) {
                    left = mid;
                } else {
                    right = mid - 1;
                }
            } 
        }

        //cout << "left : " << left << " right : " << right << endl;

        return -1;
    }
};